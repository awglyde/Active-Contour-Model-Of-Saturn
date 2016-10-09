from astropy.io import fits
from scipy import misc, ndimage
import numpy as np
import os

def denoise(im):
    noisy = im + 0.4 * im.std() * np.random.random(im.shape)
    return ndimage.gaussian_filter(noisy,2)

path = "C:/Github/ASTRON-1263/Saturn/0.01/"
save = "C:/Github/ASTRON-1263/Saturn/denoise/"

for file in os.listdir(path):
    print(file)
    if file.endswith(".fits"):
        autograb_data = fits.open(path + file)
        image_data = autograb_data[0].data
        misc.imsave(save + file + '.jpg', denoise(image_data))