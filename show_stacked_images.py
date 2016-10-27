import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

data = []



file_path = "/Users/tyler/Desktop/denoised/"
sum_img_data = 0
for file in os.listdir(file_path):
	if file.endswith(".jpg"):
		#array = np.array(Image.open(file_path + file).convert("L"))
		array = np.array(Image.open(file_path + file))
		sum_img_data += array

sum_img_data = sum_img_data/2
sum_img = Image.fromarray(sum_img_data)
plt.imshow(sum_img, cmap='Greys_r')

plt.show()