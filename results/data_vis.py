import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("/Users/tyler/Desktop/astro files/final_proj_stat.csv", 
    delimiter=',')
top_ten = len(data1)/10
top_five= len(data1)/20
data2 = data1[:top_ten]
data3 = data1[:top_five]

plt.hist(data1,1200, label="All 1101 Images")

#plt.hist(data2, 5, label="Top 10%", alpha=0.5)

plt.xlim(0,700)
plt.title("Euclidean Distances from the Good Snake to each Test Snake")
plt.xlabel('Euclidean Distances [pixels]')
plt.ylabel('Number of Images')
plt.legend(loc='upper right')
plt.show()