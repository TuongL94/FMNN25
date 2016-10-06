# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:48:27 2016

@author: as
"""
from  scipy import *
from  pylab import *
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

# not within the meshclass
# if this is not within a class at all, the self argument can be discarded

def plotWholeRoom(mesh):
    """
    surface plot of the temperature in the whole room
    input parameters: a mesh representing the whole room
                      the roomparts have to be assembled before (probably by hand)
    return: a figure object tha shows the plot
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-mesh.meshsize, mesh.xLength+mesh.meshsize, mesh.meshsize)
    Y = np.arange(-mesh.meshsize, mesh.yLength+mesh.meshsize, mesh.meshsize)
    X, Y = np.meshgrid(X, Y)
    numberOfXNodes = mesh.xLength/mesh.meshsize+1
    numberOfYNodes = mesh.yLength/mesh.meshsize+1
    Z = np.array([[mesh.nodeMatrix[i,j].funcVal for i in range(numberOfYNodes)] \
        for j in range(numberOfXNodes)])
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    # set limits for z-axis
    ax.set_zlim(np.amin(Z)-mesh.meshsize, np.amax(Z)+mesh.meshsize)
    # don't know what these two lines are for
    # x.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # don't know what these two lines are for
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()    
    return fig