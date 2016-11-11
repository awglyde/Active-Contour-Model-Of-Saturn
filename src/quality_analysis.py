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
    good_im_path = "C:/Users/tmd44/Desktop/goods/"
    
    start = time.clock()

    # determine base threshold
    good_snakes, good_files = u.get_snakes(good_im_path, good_im_path + "AutoGrab001.fits.jpg", 1)
    test_snakes, test_files = u.get_snakes(im_path, good_im_path + "AutoGrab001.fits.jpg")
 
    for i in range(0, len(test_snakes)):
        print(u.compare_snakes(good_snakes[0], test_snakes[i]), good_files[0], test_files[i])
    
    end = time.clock()
    print("delta: ", end-start)