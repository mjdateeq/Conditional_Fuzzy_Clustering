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


def Def_Centroid (data, weight, num_cen, num_feature, p):
    sumweight = np.sum(np.square(init_weight), axis=0)
    centroid=np.zeros((num_cen,num_feature))
    for i in range (num_cen):
        for j in range (num_feature):
            
            sumMM=sum((weight(:,i)**p)* data(:,j));
            centroid(i,j)=sumMM/SS; 



plt.scatter(x, y, c=labels, s=50, cmap='viridis')
plt.scatter(centers[0][0],centers[0][1],s=50, marker='x')
plt.scatter(centers[1][0],centers[1][0],s=50, marker='x')

plt.show()
