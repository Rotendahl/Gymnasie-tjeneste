from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random
def pcaHelper(vector, ys):
    dataMatrix = np.array(vector)
    myPCA = PCA(dataMatrix)
    greensX = []
    greensY = [] 
    redsX   = [] 
    redsY   = []
    i = 0
    for y in ys:
        if y == 1:
            greensX.append(myPCA.Y[i,0])
            greensY.append(myPCA.Y[i,1])
        else:           
            redsX.append(myPCA.Y[i,0])
            redsY.append(myPCA.Y[i,1])
        plt.plot(greensX,greensY,'o', color='green')
        plt.plot(redsX,redsY, 'o', color='red')
        i += 1
    plt.show()

