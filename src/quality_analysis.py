import utilities as u
import numpy as np
import time, os
from math import ceil

def get_distances(im_path, base_image, file_names, max_count=-1):
    good_snakes = u.get_snakes(im_path, [base_image] , im_path + base_image, 1)
    im_snakes = u.get_snakes(im_path, file_names, im_path + base_image, max_count)

    e_distances = []
    for i in range(0, len(im_snakes)):
        e_distances.append(u.compare_snakes(good_snakes[0], im_snakes[i]))

    return e_distances

# load and save paths
# change file paths based on which computer we're on
alex_computer = True

if alex_computer:
    im_path = "C:/Github/ASTRON-1263/data/original/"
    save_path  = "C:/Github/ASTRON-1263/data/contour/"
if not alex_computer:
    im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/jpgs/"
    save_path  = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/contours/"
    
start = time.clock()

# get a list of snakes
base_image = "AutoGrab001.fits.jpg"

file_names = []
for file in os.listdir(im_path):
    if file.endswith(".jpg"):
        file_names.append(file)

e_distances = get_distances(im_path, base_image, file_names);

print('base image: ' + base_image + "\n")
for i in range(0, len(e_distances)):
    print(file_names[i], e_distances[i])

# get the top 10 percent of the images
sort_inds = np.argsort(e_distances)
top_10_num = ceil(len(sort_inds)*0.1)

top_10 = sort_inds[0:top_10_num]

print("")
for i in range(0, len(top_10)):
    im_ind = top_10[i]
    print(base_image, file_names[im_ind], e_distances[im_ind])
    
end = time.clock()
print("\ndelta: ", end-start)