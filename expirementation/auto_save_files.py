from astropy.io import fits
from scipy import misc, ndimage
import numpy as np
import os

def denoise(im):
    '''
    Input: takes in image data array
    Returns: image data array, with gaussian denoising applied
    '''
    noisy = im + 0.4 * im.std() * np.random.random(im.shape)
    return ndimage.gaussian_filter(noisy,2)

if __name__ == "__main__":        
    # path to FITS file
    path = "C:/Github/ASTRON-1263/data/moon-fits/"

    # save images to these paths
    original = "C:/Github/ASTRON-1263/data/moon-fits/"
    denoised = "C:/Github/ASTRON-1263/data/denoise/"

    save_denoised = False
    save_original = True

    for file in os.listdir(path):
        if file.endswith(".FIT"):
            # extract image from fits
            autograb_data = fits.open(path + file)
            image_data = autograb_data[0].data

            if save_original:
                misc.imsave('C:/Github/ASTRON-1263/data/moon-green/' + file + '.jpg', image_data)

            if save_denoised:
                misc.imsave(denoised + file + '.jpg', denoise(image_data))