# coding:utf-8
## PCA

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition, datasets

from IPython.html import widgets

# Simpelt interface til scikit learns PCA implementation
def PCAprojektion(data,ndim):
    pca = decomposition.PCA(ndim)
    pca.fit(data)
    return pca

# Generering og plot af punkter/egenvektorer
def pcaplot(sigma=0.5):
    n = 130
    X,Y = 15*np.random.random_sample((n,))-7.5, 15*np.random.random_sample((n,))-7.5
    Z = -X+2*Y+5+np.random.normal(scale=sigma,size=(n,))

    fig = plt.figure(figsize=(15,8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(X, Y, Z, color='blue')

    A = np.vstack((X,Y,Z)).T
    pca = PCAprojektion(A,3)
    base = pca.components_

    initvec = np.mean(A,axis=0).reshape((3,))
    ev = pca.explained_variance_ratio_
    l = 10
    based = base*ev.reshape((3,1))

    ax.quiver(*tuple(np.concatenate((l*based[0,:]+initvec, based[0,:]))), length=l*ev[0], arrow_length_ratio=0.1, colors=(1,0,0), linewidth=2)
    ax.quiver(*tuple(np.concatenate((l*based[1,:]+initvec, based[1,:]))), length=l*ev[1], arrow_length_ratio=0.1, colors=(1,0,0), linewidth=2)
    ax.quiver(*tuple(np.concatenate((l*based[2,:]+initvec, based[2,:]))), length=l*ev[2], arrow_length_ratio=0.1, colors=(1,0,0), linewidth=2)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(elev=-160,azim=-47)
    plt.show()
    print("v_1 = %s,  forklarer %f %% af variansen\nv_2 = %s,  forklarer %f %% af variansen\nv_3 = %s,  forklarer %f %% af variansen" % (base[0,:], 100*ev[0], base[1,:], 100*ev[1], base[2,:], 100*ev[2]))


    A = np.vstack((X,Y,Z)).T
    pca = PCAprojektion(A,2)
    return pca, pca.transform(A)

# Plot projektion af punkter langs to komponenter
def inversplot(pca, projektion):
    fig = plt.figure(figsize=(15,8))
    ax = fig.add_subplot(111)

    ax.scatter(projektion[:,0],projektion[:,1])
    ax.set_xlabel(r'$\vec v_1$')
    ax.set_ylabel(r'$\vec v_2$')

    mu = np.mean(projektion, axis=0)

    ax.quiver(mu[0],mu[1],[1,0],[0,1], pivot='tail', units='xy', color='green')

    ax.axis('equal')
    plt.show()
        
        
# Indlæsning af data
olivetti = datasets.fetch_olivetti_faces(shuffle=True, random_state=np.random.RandomState(42))
faces = olivetti.data
facesim = olivetti.images

# Visning af original billeder
def plotbilleder():
    fig = plt.figure(figsize=(8*2.2,5))
    plt.gray()
    for i in range(8):
        ax = fig.add_subplot(1,8,i+1)
        ax.imshow(facesim[i])

# Visning/udregning af egenvektorer/grundansigter
def grundansigter(n=8,vis=8):
    pca = PCAprojektion(faces,n)
    eigenfaces = pca.components_
    n = pca.n_components
    size = min(vis,n)

    fig = plt.figure(figsize=(8*2.1,2.1*((size-1)//8+1)))
    plt.gray()

    for i in range(size):
        ax = fig.add_subplot((size-1)//8+1,8,i+1)
        ax.imshow(eigenfaces[i,:].reshape((64,64)))
    print("De første %i principale komponenter forklarer %f %% af dataens varians" % (pca.n_components_, 100*np.sum(pca.explained_variance_ratio_)))

# Viser et billede projiceret på et antal egenvektorer
def projektionplot():
    def projektion(Grundbilleder,Ansigt):
        pca = PCAprojektion(faces,Grundbilleder)
        billede = pca.inverse_transform(pca.transform(faces[Ansigt-1,:]))
        billede.resize((64,64))
        plt.gray()
        plt.imshow(billede)
    widget1 = widgets.BoundedIntTextWidget(value=60, min=1, max=400)
    widget2 = widgets.BoundedIntTextWidget(value=5, min=1, max=400)
    widgets.interact(projektion, Grundbilleder=widget1, Ansigt=widget2)
    
