import os
import numpy as np
import matplotlib.pyplot as plt
import time
#Image/FITS Processing libraries
from PIL import Image
from astropy.io import fits
from scipy import misc, ndimage
#Active Contour libraries
from skimage.filters import gaussian
from skimage.segmentation import active_contour

# from auto_crop_images:
def determine_threshold(im_arr, x_min, x_max, y_min, y_max, confidence_interval = 0):
    ''' 
    Determine a cutoff threshold provided an image and a 
    region of noise_region bound by x_min, x_max, y_min, and y_max.
    '''
    noise_region = im_arr[x_min:x_max, y_min:y_max]
    return noise_region.mean() + confidence_interval*noise_region.std()

def apply_high_pass(im_arr, cutoff_frequency, new_value):
    '''
    Replaces all values in the array that are equal to or below the cutoff frequency
    by a new value.
    '''
    replace_inds = np.where(im_arr <= cutoff_frequency)
    im_arr[replace_inds] = new_value
    return

def crop_image(im_arr, x_min, x_max, y_min, y_max):
    '''
    Crop image based on given x and y values. 
    '''
    return im_arr[x_min:x_max, y_min:y_max]

def determine_crop_size(im_arr, threshold, padding = 0):
    '''
    Determines what the size of the image should be based on the
    cutoff threshold value.
    '''

    valid_indicies = np.where(im_arr > threshold)
    
    x_min = valid_indicies[0].min() - padding
    x_max = valid_indicies[0].max() + padding
    y_min = valid_indicies[1].min() - padding
    y_max = valid_indicies[1].max() + padding

    # force the x values to be in the correct domain
    x_min = 0 if (x_min < 0) else x_min
    x_max = len(im_arr[1,:]) if x_max > len(im_arr[1,:]) else x_max

    # force the y values to be in the correct range
    y_min = 0 if (y_min < 0) else y_min
    y_max = len(im_arr[1,:]) if y_max > len(im_arr[1,:]) else y_max

    return (x_min, x_max, y_min, y_max)    

def display_image(im_arr):
    '''
    Display image on plot for testing purposes.
    '''
    plt.imshow(im_arr, cmap="Greys_r")
    plt.grid()
    plt.show()

def auto_crop_images():
    '''
    formerly this was the if __main__ function in the auto_crop_images library
    
    running this will take the images from ims_path and put them in the save_path
    '''
    # path variables
    ims_path = "C:/Github/ASTRON-1263/data/denoise/"
    save_path = "C:/Github/ASTRON-1263/data/cropped/"

    # get threshold value      
    base_im = np.array(Image.open(ims_path + "AutoGrab001.fits.jpg")) 
    threshold = determine_threshold(base_im, 0, len(base_im), 0, 150, confidence_interval = 10) 

    for file in os.listdir(ims_path):
        if file.endswith(".jpg"):
            # load image
            im_arr = np.array(Image.open(ims_path + file))

            # get the size to crop to
            x_min, x_max, y_min, y_max = determine_crop_size(im_arr, threshold, padding = 30)

            # crop image
            cropped_im_arr = crop_image(im_arr, x_min, x_max, y_min, y_max)

            # save Image
            im = Image.fromarray(cropped_im_arr)
            im.save(save_path + file)

# from auto_save_files:

def denoise(im):
    '''
    Input: takes in image data array
    Returns: image data array, with gaussian denoising applied
    '''
    noisy = im + 0.4 * im.std() * np.random.random(im.shape)
    return ndimage.gaussian_filter(noisy,2)

def auto_save_files():
    '''
    formerly the __main__ function from the auto_save_files.py script
    running this will take FITS files from path and save the jpgs in original, 
    and denoised versions in denoised
    '''
    # path to FITS file
    path = "C:/Github/ASTRON-1263/data/saturn-0.01/"

    # save images to these paths
    original = "C:/Github/ASTRON-1263/data/original/"
    denoised = "C:/Github/ASTRON-1263/data/denoise/"

    save_denoised = False
    save_original = True

    for file in os.listdir(path):
        if file.endswith(".fits"):
            # extract image from fits
            autograb_data = fits.open(path + file)
            image_data = autograb_data[0].data

            if save_original:
                misc.imsave(original + file + '.jpg', image_data)

            if save_denoised:
                misc.imsave(denoised + file + '.jpg', denoise(image_data))

#from contour_saturn.py:

def get_cropped_image(im_file, threshold):
    '''
    Crops the image.
    '''
    # get threshold value from the denoised image
    im_array = np.array(Image.open(im_file)) 
    denoise_im = denoise(im_array)

    # determine the new crop size
    x_min, x_max, y_min, y_max = determine_crop_size(denoise_im, threshold, padding=30)

    # crop the original image based on the crop size of the denoised image
    cropped_im = crop_image(im_array, x_min, x_max, y_min, y_max)
    return cropped_im

def get_init_snake(im_arr):
    '''
    Determines the initial shape of the snake.
    '''
    # center shape on image
    x_center = len(im_arr[0,:])/2
    y_center = len(im_arr[:,0])/2

    s = np.linspace(0, 2*np.pi, 1000)
    x = x_center + 200*np.cos(s)
    y = y_center + 200*np.sin(s)

    return np.array([x, y]).T
    
def fit_snake(im_arr, init_snake, auto_blur = False):
    '''
    Fits the intial snake value to the image passed in.
    '''
    fit_im = []
    if auto_blur:
        fit_im = gaussian(im_arr, 4)
    else:
        fit_im = im_arr
    return active_contour(fit_im, init_snake, alpha=0.015, beta=10, gamma=0.001)

def display_snake_fig(im_arr, init_snake, final_snake, show_fig = False, save_fig = True, save_file = "", show_snake_region=True):
    '''
    Save a figure demonstrating the image, the initial snake, and the final snake.
    If save_fig is true, save_file must also be defined.
    '''
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    plt.gray()
    ax.imshow(im_arr)
    if show_snake_region:
        ax.plot(init_snake[:, 0], init_snake[:, 1], '--r', lw=3)
    ax.plot(final_snake[:, 0], final_snake[:, 1], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, im_arr.shape[1], cropped_im.shape[0], 0])

    if show_fig:
        plt.show()
    
    if save_fig:
        plt.savefig(save_file, bbox_inches='tight')

    # need to close all matplotlib figures
    plt.close("all")

    return

def contour_saturn():
    '''formerly the __main__ function from contour_saturn.py
    running this will take jpgs from im_path, crop them, and apply a contour
    it will save jpg images with the contours overlaid in save_path
    '''
    # load and save paths
    # change file paths based on which computer we're on
    alex_computer = False
    if alex_computer:
        im_path = "C:/Github/ASTRON-1263/data/original/"
        save_path  = "C:/Github/ASTRON-1263/data/contour/"
    if not alex_computer:
        im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/jpgs/"
        save_path  = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/contours/"

    start = time.clock()

    # determine base threshold
    base_im = np.array(Image.open(im_path + "AutoGrab001.fits.jpg"))
    base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

    for file in os.listdir(im_path):
        if file.endswith(".jpg"):
            # crop image
            cropped_im = get_cropped_image(im_path + file, base_threshold)

            # get initial snake shape
            init_snake = get_init_snake(cropped_im)

            # determine contour around saturn
            final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)

            # save image
            display_snake_fig(cropped_im, init_snake, final_snake, show_fig = False, save_fig = True, save_file=(save_path + file))
    end = time.clock()
    print("delta: ", end-start)

# from compare_contours.py:

def get_snakes(im_path, base_filename, max_count=-1):
	# determine base threshold
	base_im = np.array(Image.open(base_filename))
	base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

	count = 0
	snakes_list = []
	file_list = []
	for file in os.listdir(im_path):
		if count == max_count:
			break
		if file.endswith(".jpg"):
			count += 1
			# crop image
			cropped_im = get_cropped_image(im_path + file, base_threshold)
			
			# get initial snake shape
			init_snake = get_init_snake(cropped_im)

			# determine contour around saturn
			final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)
			snakes_list.append(final_snake)
			file_list.append(file)
	return snakes_list, file_list

def compare_snakes(generic_snake_left, generic_snake_right):
    difference = generic_snake_right - generic_snake_left
    sum_distances_squared = np.sum(difference**2)
    return np.sqrt(sum_distances_squared)

def compare_contours():
	'''
	formerly the __main__ from the compare_contours.py file

	running this will read images from good_im_path and compare the contours to images from
	im_path. It currently also prints out the contour arrays for the good and the bad images,
	with their respective file names.
	'''
	# load and save paths
	# change file paths based on which computer we're on
	alex_computer = False
	if alex_computer:
		good_im_path = "C:/Github/ASTRON-1263/data/original/" 
		im_path = "C:/Github/ASTRON-1263/data/original/"
		save_path  = "C:/Github/ASTRON-1263/data/contour/"
	if not alex_computer:
		good_im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/goods/"
		im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/jpgs/"
		save_path  = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/contours/"
		bad_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/bads/"

	start = time.clock()
	
	good_snakes, good_files = get_snakes(good_im_path, good_im_path + "AutoGrab001.fits.jpg", 1)
	test_snakes, test_files = get_snakes(im_path, good_im_path + "AutoGrab001.fits.jpg")

	for i in range(0, len(test_snakes)):
		print(compare_snakes(good_snakes[0], test_snakes[i]), good_files[0], test_files[i])


	end = time.clock()
	print("delta: ", end-start)

# from show_stacked_images:
def show_stacked_images():
	'''
	formerly the __main__ function from show_stacked_images.py

	running this will print out a stacked version of all of the images in file_path
	'''
	data = []
	file_path = "/Users/tyler/Desktop/denoised/"
	sum_img_data = 0
	for file in os.listdir(file_path):
		if file.endswith(".jpg"):
			#array = np.array(Image.open(file_path + file).convert("L"))
			array = np.array(Image.open(file_path + file))
			sum_img_data += array

	sum_img_data = sum_img_data/2
	sum_img = Image.fromarray(sum_img_data)
	plt.imshow(sum_img, cmap='Greys_r')

	plt.show()