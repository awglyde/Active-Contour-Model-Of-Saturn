import numpy as np
import matplotlib.pyplot as plt

plt.clf()

data1 = np.genfromtxt("/Users/tyler/Desktop/astro files/final_proj_stat.csv", 
    delimiter=',')
top_ten = len(data1)/10
top_five= len(data1)/20
data2 = np.sort(data1)[:top_ten]
data3 = np.sort(data1)[:top_five]

bins = np.arange(0,700,35)

plt.subplot(3,1,1)
plt.hist(data1,bins=bins, label="All 1101 Images")
plt.title("Distribution of Euclidean Dist. from the Good Snake to each Test Snake")
plt.ylabel('Number of Images')
plt.xlim(0,700)
plt.ylim(0,210)
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(3,1,2)
#plt.hist(data2, bins=np.arange(0,200,5), label="Closest 10%", color='green')
plt.hist(data2, bins=bins, label="Closest 10%", color='green')
plt.legend(loc='upper right')
plt.ylabel('Number of Images')
plt.grid(True)

plt.subplot(3,1,3)
plt.hist(data1,bins=bins, label="All 1101 Images")
plt.hist(data2, bins=bins, label="Closest 10%", alpha=1)
plt.xlabel('Euclidean Distances [pixels]')
plt.ylabel('Number of Images')
plt.ylim(0,210)
plt.legend(loc='upper right')
plt.grid(True)


plt.show()