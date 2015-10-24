# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from skimage import io

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.pipeline import Pipeline
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.ticker import LogLocator

from IPython.html import widgets

# Remove those annoying DeprecationWarnings:
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

### Opsætning ###
plt.style.use('bmh')
cmap = plt.cm.Set1
cseq = [plt.cm.Set1(i) for i in np.linspace(0, 1, 9, endpoint=True)]
plt.rcParams['axes.color_cycle'] = cseq


### Polynomium ###

def true_poly(x):
    return .05*x**3. + 0.02*x**2. - 1.3*x + 2.7


def ukendte_data(antal_data=17, seed=30):
    np.random.seed(seed)

    scale = 10.

    x = np.linspace(-7.5, 7.5, antal_data)
    x += scale*np.random.rand(antal_data)/5 - 0.5*scale/5
    x.sort()

    y = true_poly(x)
    y += scale*np.random.rand(antal_data) - 0.5*scale

    return x,y



def plot_data(x, y, titel=""):

    fig = plt.figure(42)
    ax = fig.add_subplot(111)

    if titel:
        ax.set_title(titel)

    ax.plot(x, y, ls="", marker="o", alpha=.7, mec=cseq[0])

    ax.set_ylim(-30,40)
    ax.set_xlim(-10,10)

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")




def poly_data(n_points = 17):
    np.random.seed(23)

    scale = 5.

    x = np.linspace(-7,7,n_points)
    x += scale*np.random.rand(n_points) - 0.5*scale
    x.sort()

    y = true_poly(x)
    y += scale*np.random.rand(n_points) - 0.5*scale

    return x,y



### k Nearest Neighbour ###


def add_noise(x, y, scale = .5):
    np.random.seed(23)

    n_points = len(x)

    x2 = x + scale*np.random.rand(n_points) - 0.5*scale
    x2.sort()

    y2 = y + scale*np.random.rand(n_points) - 0.5*scale

    return x2,y2


def fit_kNN(x, y, k, form):
    kNN = KNeighborsRegressor(n_neighbors=k, weights=form)
    kNN.fit(x[:,None], y)

    return kNN


def kNN(x, fit):
    return fit.predict(x[:, None])


def plot_kNN(x, fit, data=None):

    if not data:
        xd, yd = ukendte_data()

    fig, ax = plt.subplots()

    ax.plot(data[0], data[1], ls="", marker="o", alpha=.7, mec=cseq[0])

    ax.plot(x, kNN(x,fit))

    ax.set_ylim(-30,40)
    ax.set_xlim(-10,10)

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")


def plot_interaktiv_kNN(x, naboer=(1,17)):

    def f(k, metode):
        xd, yd = ukendte_data()

        fit = fit_kNN(xd, yd, k, metode)
        plot_kNN(x, fit, data=(xd,yd))


    k_widget = widgets.IntSlider(min=naboer[0], max=naboer[1],
                                                step=1, value=naboer[0])

    m_widget=widgets.RadioButtonsWidget(values=["uniform", "distance"],
                                      value="uniform")

    _ = widgets.interact(f, k=k_widget,metode=m_widget)

    #widgets.interact(f, k=widgets.IntSliderWidget(min=naboer[0], max=naboer[1],
    #                                              step=1, value=naboer[0]),
    #                 metode=("uniform", "distance"))



def plot_interaktiv_kNN_klassifikation(X, y, naboer=(1,50), res=.02):

    # Save classifications for later use:
    calculated_k = {"uniform": {}, "distance": {}}

    xl, xh = np.ceil(X[:,0].min() - 1), np.floor(X[:,0].max() + 1)
    yl, yh = np.ceil(X[:,1].min() - 1), np.floor(X[:,1].max() + 1)


    # Create grid to calculate the decision boundary on:
    xx, yy = np.meshgrid(np.arange(xl, xh, res),
                        np.arange(yl, yh, res))

    def f(k, metode):

        clf = KNeighborsClassifier(k, weights=metode)
        clf.fit(X, y)

        #Plot data:
        fig, ax = plt.subplots()

        ax.scatter(X[:,0], X[:,1], s=25, c=plt.cm.Set2(y/7),
                   edgecolor=plt.cm.gray(.95), lw=0.5, zorder=100)

        try:
            Z = calculated_k[metode][k]

        except KeyError:
            Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

            Z = Z.reshape(xx.shape)

            # Save the calculation:
            calculated_k[metode][k] = Z


        # Plot image:
        ax.matshow(Z, cmap=plt.cm.Pastel2, vmax=7, origin="lower",
                  extent=[xl, xh, yl, yh], aspect="auto")
        ax.xaxis.set_ticks_position('bottom')
        ax.grid(False)



    k_widget = widgets.IntSliderWidget(min=naboer[0], max=naboer[1],
                                                step=1, value=naboer[0])

    m_widget=widgets.RadioButtonsWidget(values=["uniform", "distance"],
                                      value="uniform")

    _ = widgets.interact(f, k=k_widget,metode=m_widget)


### K-means clustering ###

def own_Kmeans(X, klynger, start=None):

    if start is None:
        indices = np.random.choice(len(X), klynger, replace=False)
        centers = X[indices]

        xl, xh = X[:,0].min(), X[:,0].max()
        yl, yh = X[:,1].min(), X[:,1].max()

        centers = np.asarray([np.random.rand(klynger)*(xh-xl)+xl,
                              np.random.rand(klynger)*(yh-yl)+yl]).T
    else:
        centers = start

    locations = []
    locations.append(centers)
    labels = []

    converged = False
    counter = 0

    while not converged:

        dists = np.empty((len(centers),len(X)))
        for i,c in enumerate(centers):
            dists[i] = np.linalg.norm(X-c, axis=1)

        labels.append(np.argmin(dists, axis=0))

        new_centers = []
        for c in range(klynger):
            p = X[np.where(labels[-1] == c)]
            new_centers.append(np.mean(p, axis=0))

        new_centers = np.asarray(new_centers)

        cdists = np.linalg.norm(centers-new_centers)
        centers = new_centers

        locations.append(centers)

        #print(cdists)

        if np.sum(cdists) < 1e-6:
            converged = True

        else:
            counter += 1

        if counter > 50:
            #print("No convergence! Forcing stop!")
            counter, locations, labels = own_Kmeans(X, klynger)
            converged = True

    return counter, np.array(locations), np.array(labels)



def plot_interaktiv_Kmeans(X, klynger):

    counter, locations, labels = own_Kmeans(X, klynger)

    #def on_button_clicked(b):
    #    print("Button clicked.")
    #    counter, locations, labels = own_kmeans(X, klynger)
    #
    #    iter_widget.value = 0

    def f(iteration, spor):

        fig, ax = plt.subplots()

        centers = locations[iteration]
        l = labels[iteration]

        ax.scatter(X[:,0], X[:,1], s=25, c=plt.cm.Set2(l/7),
                   edgecolor=plt.cm.gray(.95), lw=0.5)
        ax.scatter(centers[:,0], centers[:,1], marker='x', s=50,
                linewidths=3, color=plt.cm.Reds(.75), zorder=15)


        if spor:
            for i in range(klynger):

                ax.plot(locations[:iteration+1,i,0], locations[:iteration+1,i,1],
                     marker="", ls="--", c=plt.cm.Reds(.75))


    iter_widget = widgets.IntSliderWidget(min=0, max=counter,
                                          step=1, value=0)

    spor_widget=widgets.CheckboxWidget()


    _ = widgets.interact(f, iteration=iter_widget, spor=spor_widget)


    #button = widgets.ButtonWidget(description="Click Me!")
    #button.set_css("margin-left", "2em")

    #button.on_click(on_button_clicked)
    #display(button)






class Billede:

    def __init__(self, billede):
        self.billede = io.imread(billede)
        self.dims = self.billede.shape


    @property
    def billede_til_pixels(self):
        dx,dy,dz = self.dims
        dz = 3 # workaround in case of PNGs.
        self.pixels = self.billede[:,:,:3].reshape(dx*dy,dz)
        data = pd.DataFrame(data=self.pixels, columns=["r","g","b"])

        return data

    @property
    def pixels_til_billede(self):
        dx,dy,dz = self.dims
        dz = 3 # workaround in case of PNGs.
        self.nyt_billede = np.copy(self.billede)
        self.nyt_billede[:,:,:3] = self.pixels.reshape(dx,dy,dz)

        return self.nyt_billede


    def reducer_farver(self, kmeans):
        labels = kmeans.labels_
        centre = kmeans.cluster_centers_
        pixels = np.copy(self.pixels)
        #nyt_billede = copy(self.pixels)
        for label in np.unique(labels):
            idx = np.where(labels == label)
            #nyt_billede[idx] = centre[label]
            pixels[idx] = centre[label]

        dx,dy,dz = self.dims
        dz = 3 # workaround in case of PNGs.
        red = np.copy(self.billede)
        red[:,:,:3] = pixels.reshape(dx,dy,dz)
        return red



def plot_farver(billede, centre=None):

    pixels = billede.billede_til_pixels

    colours = ["r", "g", "b"]
    cnames = ["Rød", "Grøn", "Blå"]

    cmap = plt.cm.Blues

    fig, ax = plt.subplots(1,3, figsize=(12,6))

    extent = [0, 255, 0, 255]

    for i in range(2):
        for j in range(i+1,3):

            c1 = colours[i]
            c2 = colours[j]

            c = i + j - 1

            H, xedges, yedges = np.histogram2d(pixels[c2], pixels[c1], 256,
                                               range=[[extent[0], extent[1]],
                                                      [extent[2], extent[3]]])


            H[np.where(H < 1)] = 0.1

            cax = ax[c].imshow(H, extent=extent, aspect='equal', origin='lower',
                               cmap = cmap,
                               norm=LogNorm(vmin=1, vmax=np.nanmax(H)), zorder=10)

            ax[c].set_xlabel(cnames[i])
            ax[c].set_ylabel(cnames[j])

            if centre is not None:
                ax[c].scatter(centre[:,i], centre[:,j], marker='x', s=50,
                              linewidths=3, color=plt.cm.Reds(.9), zorder=15)

            ax[c].set_ylim(0,256)
            ax[c].set_xlim(0,256)

    fig.tight_layout()


def kMeans(billede, antal_klynger=5, n_init=1):
    kmeans = KMeans(n_clusters=antal_klynger, n_init=n_init)
    kmeans.fit(billede.billede_til_pixels)

    return kmeans


def plot_kMeans(billede, kmeans, n_init=1):

    #kmeans = kMeans(billede, klynger, n_init=1)
    centre = kmeans.cluster_centers_

    #print(centre)

    plot_farver(billede, centre)


def plot_reducerede_farver(billede, kmeans, n_init=1):

    #kmeans = kMeans(billede, klynger, n_init=1)

    red_billede = billede.reducer_farver(kmeans)

    plt.imshow(red_billede)

