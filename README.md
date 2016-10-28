# ASTRON-1263
ASTRON 1263 - Final Project - Fast Image and Automatic Analysis of Saturn

## File Description

#### test/denoised_saturn_gif.gif

This GIF file demonstrates the seeing affects caused by turbulance in the atmosphere when viewing Saturn at low altitudes.

#### test/auto_save_files.py

This script takes a list of fits files with one image extracts it and saves them it as a jpg.

#### test/auto_crop_images.py

This script detects a cutoff threshold for a given region of noise and automatically crops the given set of images to remove that noise. This is useful for Saturn images because Saturn, which is mostly light grey, is surrounded by dark gray pixels. Autocropping each image saves time and allows us to quicken our computer vision techniques.

#### test/contour_saturn.py

This script crops each image and determines the contour of saturn within the cropped image.


#### test/compare_contour.py

This script compares the contours of images of Saturn to contours on user defined "good" images.
