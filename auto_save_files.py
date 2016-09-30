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


path = "C:/Users/tmd44/Desktop/images/" #location of FITS files to take in
save = "C:/Users/tmd44/Desktop/denoise/" #location to save denoised images

for file in os.listdir(path):
    autograb_data = fits.open(path + file)
    image_data = autograb_data[0].data
    misc.imsave(save + file + '.jpg', denoise(image_data))