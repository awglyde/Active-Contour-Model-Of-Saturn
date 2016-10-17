import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def determine_threshold(im_arr, x_min, x_max, y_min, y_max, confidence_interval = 10):
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

# path variables
ims_path = "C:/Github/ASTRON-1263/data/denoise/"
save_path = "C:/Github/ASTRON-1263/data/cropped/"

# get threshold value      
base_im = np.array(Image.open(ims_path + "AutoGrab001.fits.jpg")) 
threshold = determine_threshold(base_im, 0, len(base_im), 0, 150) 

for file in os.listdir(ims_path):
    if file.endswith(".jpg"):
        # load image
        im_arr = np.array(Image.open(ims_path + file))

        # get the size to crop to
        x_min, x_max, y_min, y_max = determine_crop_size(im_arr, threshold, 30)

        # crop image
        cropped_im_arr = crop_image(im_arr, x_min, x_max, y_min, y_max)

        # save Image
        im = Image.fromarray(cropped_im_arr)
        im.save(save_path + file)
