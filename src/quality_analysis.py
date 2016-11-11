import utilities as u
import os
import numpy as np
import time
#Image/FITS Processing libraries
from PIL import Image

if __name__ == "__main__":
    # load and save paths
    # change file paths based on which computer we're on
    alex_computer = False
    if alex_computer:
        im_path = "C:/Github/ASTRON-1263/data/original/"
        save_path  = "C:/Github/ASTRON-1263/data/contour/"
    if not alex_computer:
        im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/jpgs/"
        save_path  = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/contours/"
        
    im_path = "C:/Users/tmd44/Desktop/small-denoise/"
    save_path = "C:/Users/tmd44/Desktop/contours/"
    start = time.clock()

    # determine base threshold
    base_im = np.array(Image.open(im_path + "AutoGrab001.fits.jpg"))
    base_threshold = u.determine_threshold(u.denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

    for file in os.listdir(im_path):
        if file.endswith(".jpg"):
            # crop image
            cropped_im = u.get_cropped_image(im_path + file, base_threshold)

            # get initial snake shape
            init_snake = u.get_init_snake(cropped_im)

            # determine contour around saturn
            final_snake = u.fit_snake(cropped_im, init_snake, auto_blur = True)

            # save image
            u.display_snake_fig(cropped_im, init_snake, final_snake, show_fig = False, save_fig = True, save_file=(save_path + file))
    end = time.clock()
    print("delta: ", end-start)