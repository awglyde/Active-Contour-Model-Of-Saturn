import utilities as u
import numpy as np
import time
from math import ceil
        
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
    im_snakes, im_files = u.get_snakes(im_path, good_im_path + "AutoGrab001.fits.jpg")
 
    e_distances = []
    for i in range(0, len(im_snakes)):
       e_distances.append(u.compare_snakes(good_snakes[0], im_snakes[i]))
    
    # get the top 10 percent of the images
    sort_inds = np.argsort(e_distances)
    top_10_num = ceil(len(sort_inds)*0.1)
    
    top_10 = sort_inds[0:top_10_num]
    
    for i in range(0, len(top_10)):
        im_ind = top_10[i]
        print(good_files[0], im_files[im_ind], e_distances[im_ind])
        
    end = time.clock()
    print("delta: ", end-start)