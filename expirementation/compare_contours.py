from auto_save_files import denoise
from auto_crop_images import determine_threshold, determine_crop_size, crop_image
from contour_saturn import get_cropped_image, get_init_snake, fit_snake
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from scipy import misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import os

def get_snakes(im_path, base_filename, max_count=-1):
	# determine base threshold
	base_im = np.array(Image.open(base_filename))
	base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

	count = 0
	snakes_list = []
	file_list = []
	for file in os.listdir(im_path):
		if count == max_count:
			break
		if file.endswith(".jpg"):
			count += 1
			# crop image
			cropped_im = get_cropped_image(im_path + file, base_threshold)
			
			# get initial snake shape
			init_snake = get_init_snake(cropped_im)

			# determine contour around saturn
			final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)
			snakes_list.append(final_snake)
			file_list.append(file)
	return snakes_list, file_list

def compute_generic_representation(snake):
	pass

def compare_snakes(generic_snake_left, generic_snake_right):
    difference = generic_snake_right - generic_snake_left
    sum_distances_squared = np.sum(difference**2)
    return np.sqrt(sum_distances_squared)

def is_good_image(snake_diff, threshold):
    pass

if __name__ == "__main__":
	# load and save paths
	# change file paths based on which computer we're on
	alex_computer = False
	if alex_computer:
		good_im_path = "C:/Github/ASTRON-1263/data/original/" 
		im_path = "C:/Github/ASTRON-1263/data/original/"
		save_path  = "C:/Github/ASTRON-1263/data/contour/"
	if not alex_computer:
		im_path = "C:/Users/tmd44/Desktop/small-denoise/"
		save_path = "C:/Users/tmd44/Desktop/contours/"
		good_im_path = "C:/Users/tmd44/Desktop/goods/"
  
	start = time.clock()
	
	good_snakes, good_files = get_snakes(good_im_path, good_im_path + "AutoGrab001.fits.jpg", 1)
	test_snakes, test_files = get_snakes(im_path, good_im_path + "AutoGrab001.fits.jpg")

	for i in range(0, len(test_snakes)):
		print(compare_snakes(good_snakes[0], test_snakes[i]), good_files[0], test_files[i])

	end = time.clock()
	print("delta: ", end-start)