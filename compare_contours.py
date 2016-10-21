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
import os

def get_snakes(im_path, base_filename, max_count=-1):
	# determine base threshold
	base_im = np.array(Image.open(im_path + "AutoGrab001.fits.jpg"))
	base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

	count = 0
	snakes_list = []
	for file in os.listdir(im_path):
		if count == max_count:
			break
		if file.endswith(".jpg"):
			print(file)
			count += 1
			# crop image
			cropped_im = get_cropped_image(im_path + file, base_threshold)

			# get initial snake shape
			init_snake = get_init_snake(cropped_im)

			# determine contour around saturn
			final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)
			snakes_list.append(final_snake)
	return snakes_list

def compute_generic_representation(snake):
	pass

def compare_snakes(generic_snake_left, generic_snake_right):
    pass

def is_good_image(snake_diff, threshold):
    pass

if __name__ == "__main__":
	# load and save paths
	# change file paths based on which computer we're on
	alex_computer = True
	if alex_computer:
		good_im_path = "C:/Github/ASTRON-1263/data/original/" 
		im_path = "C:/Github/ASTRON-1263/data/original/"
		save_path  = "C:/Github/ASTRON-1263/data/contour/"
	if not alex_computer:
		good_im_path = "/Users/tyler/Documents/Pitt Stuf/2016-2017/Fall Semester/Astro 1263/goods/"
		im_path = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/jpgs/"
		save_path  = "/Users/tyler/Documents/Pitt Stuff/2016-2017/Fall Semester/Astro 1263/contours/"

	start = time.clock()
	
	good_snakes = get_snakes(good_im_path, "AutoGrab030.fits.jpg", 10)
	test_snakes = get_snakes(im_path, "AutoGrab001.fits.jpg", 10)

	end = time.clock()
	print("delta: ", end-start)