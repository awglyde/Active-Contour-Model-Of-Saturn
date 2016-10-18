from auto_save_files import denoise
from auto_crop_images import determine_threshold, determine_crop_size, crop_image
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from scipy import misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def get_cropped_image(im_file):
    '''
    Crops the image.
    '''
    # get threshold value from the denoised image
    im_array = np.array(Image.open(im_file)) 
    denoise_im = denoise(im_array)

    threshold = determine_threshold(denoise_im, 0, len(im_array), 0, 150, confidence_interval=10)

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
    
def fit_snake(im_arr, init_shape, auto_blur = False):
    '''
    Fits the intial snake value to the image passed in.
    '''
    fit_im = []
    if auto_blur:
        fit_im = gaussian(im_arr, 3)
    else:
        fit_im = im_arr
    return active_contour(fit_im, init_snake, alpha=0.015, beta=10, gamma=0.001)

def display_snake_fig(im_arr, init_snake, final_snake, show_fig = True, save_fig = False, save_file = ""):
    '''
    Save a figure demonstrating the image, the initial snake, and the final snake.
    If save_fig is true, save_file must also be defined.
    '''
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    plt.gray()
    ax.imshow(im_arr)
    ax.plot(init_snake[:, 0], init_snake[:, 1], '--r', lw=3)
    ax.plot(final_snake[:, 0], final_snake[:, 1], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, im_arr.shape[1], cropped_im.shape[0], 0])

    if show_fig:
        plt.show()
    
    if save_fig:
        plt.savefig(save_file)

    return

if __name__ == "__main__":
    # load and save paths
    data_path = "C:/Github/ASTRON-1263/data/"
    original_path = "C:/Github/ASTRON-1263/data/original/"

    # crop image
    cropped_im = get_cropped_image(original_path + "AutoGrab001.fits.jpg")

    # get initial snake shape
    init_snake = get_init_snake(cropped_im)

    # determine contour around saturn
    final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)

    # save image
    display_snake_fig(cropped_im, init_snake, final_snake, data_path + "fig.jpg", )