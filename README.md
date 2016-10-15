# ASTRON-1263
ASTRON 1263 - Final Project - Fast Image and Automatic Analysis of Saturn

## File Description

#### denoised_saturn_gif.gif

This GIF file demonstrates the seeing affects caused by turbulance in the atmosphere when viewing Saturn at low altitudes.

#### auto_save_files.py

This script takes a list of fits files with one image extracts it and saves them it as a jpg.

#### auto_crop_images.py

This script detects a cutoff threshold for a given region of noise and automatically crops the given set of images to remove that noise. This is useful for Saturn images because Saturn, which is mostly light grey, is surrounded by dark gray pixels. Autocropping each image saves time and allows us to quicken our computer vision techniques.
