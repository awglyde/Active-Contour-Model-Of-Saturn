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

def return_good_snake(good_im_path, base_filename):
	# determine base threshold
	base_im = np.array(Image.open(good_im_path + base_filename))
	base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

	for file in os.listdir(good_im_path):
		# crop image
		cropped_im = get_cropped_image(good_im_path + file, base_threshold)

		# get initial snake shape
		init_snake = get_init_snake(cropped_im)

		# determine contour around saturn
		final_snake = fit_snake(cropped_im, init_snake, auto_blur = True)
	return final_snake

def return_snake_as_array(im_path, base_filename, max_count=-1):
	# determine base threshold
	base_im = np.array(Image.open(im_path + base_filename))
	base_threshold = determine_threshold(denoise(base_im), 0, len(base_im), 0, 150, confidence_interval = 10)

	count = 0
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

	good_snake = return_good_snake(good_im_path, "AutoGrab030.fits.jpg")
	test_snake = return_snake_as_array(im_path, "AutoGrab001.fits.jpg", 100)

	diff = good_snake - test_snake

	if np.sum(diff) > threshold:
		good_pic = Image.fromarray()

	end = time.clock()
	print("delta: ", end-start)