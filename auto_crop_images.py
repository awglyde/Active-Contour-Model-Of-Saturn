import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ims_path = "C:/Github/ASTRON-1263/Saturn/denoise/"
save_path = "C:/Github/ASTRON-1263/Saturn/cropped/"

def determine_threshold(im_arr, x_min, x_max, y_min, y_max):
    ''' 
    Determine a cutoff threshold provided an image and a 
    region of noise bound by x_min, x_max, y_min, and y_max.
    '''
    noise = im_arr[x_min:x_max, y_min:y_max]
    confidence_interval = 8
    return noise.mean() + confidence_interval*noise.std()

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

    return (x_min, x_max, y_min, y_max)    

def display_image(im_arr):
    '''
    Display image on plot for testing purposes.
    '''
    plt.imshow(im_arr, cmap="Greys_r")
    plt.grid()
    plt.show()

# get threshold value      
base_im = np.array(Image.open(ims_path + "AutoGrab001.fits.jpg")) 
threshold = determine_threshold(base_im, 0, len(base_im), 0, 150) 

for file in os.listdir(ims_path):
    if file.endswith(".jpg"):
        # load image
        im_arr = np.array(Image.open(ims_path + file))

        # get the size to crop to
        x_min, x_max, y_min, y_max = determine_crop_size(im_arr, threshold)

        # crop image
        cropped_im_arr = im_arr[x_min:x_max, y_min:y_max]

        # save Image
        im = Image.fromarray(cropped_im_arr)
        im.save(save_path + file)
