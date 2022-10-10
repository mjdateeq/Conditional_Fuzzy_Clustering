# Not completed

from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

## Small dataset for testing purposes
x = [0, 0.4, 0.3, 0.67, 0.87, 0.97, 1.2, 2, 2.4, 2.3, 2.67, 2.87, 2.97, 3.2]
y = [0.2, 0.67, 0.7, 0.45, 0.95, 1.05, 1.1, 2.5, 2.67, 2.7, 2.45, 2.95, 3.05, 3.1]

data =  list(zip(x,y))
num_data=len(data)
num_feature=np.ndim((np.array(data)))
# generate inital weights
init_weight = np.random.rand(num_data, num_feature)
k=2
centroid = []

def Def_Centroid (data, weight, num_cen, num_feature):
    centroid=np.zeros((num_cen,num_feature))

    for i in range (num_cen):
        for j in range (num_feature):
            SS=np.sum(np.square(weight[:,i]))
            sumMM=np.sum(np.square(init_weight[:,i])*data[:,j])
            centroid[i,j]=sumMM/SS

    return centroid

arr = np.array (data)
centroid = Def_Centroid (arr, init_weight, k, num_feature)

plt.scatter(x, y, c=labels, s=50, cmap='viridis')
plt.scatter(centroid[0][0],centroid[0][1],s=50, marker='x')
plt.scatter(centroid[1][0],centroid[1][0],s=50, marker='x')

plt.show()
