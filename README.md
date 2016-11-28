# ASTRON-1263
ASTRON 1263 - Final Project - Fast Image and Automatic Analysis of Saturn

## File Description

#### src/quality_analysis.py

This script determines "good" quality saturn images out of a set of jpegs provided to the script. "Good" means that the rings of saturn have not been warped by seeing affects in the atmosphere.

#### src/utilities.py

This script contains a bunch of functions that are useful when analyzing the quality of saturn and for debugging purposes.

#### expirementation/denoised_saturn_gif.gif

This GIF file demonstrates the seeing affects caused by turbulance in the atmosphere when viewing Saturn at low altitudes.

#### expirementation/auto_save_files.py

This script takes a list of fits files with one image extracts it and saves them it as a jpg.

#### expirementation/auto_crop_images.py

This script detects a cutoff threshold for a given region of noise and automatically crops the given set of images to remove that noise. This is useful for Saturn images because Saturn, which is mostly light grey, is surrounded by dark gray pixels. Autocropping each image saves time and allows us to quicken our computer vision techniques.

#### expirementation/contour_saturn.py

This script crops each image and determines the contour of saturn within the cropped image.


#### test/compare_contour.py

This script compares the contours of images of Saturn to contours on user defined "good" images.
