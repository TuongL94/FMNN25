# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:18:44 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

import scipy as sp
import pylab as pl
import numpy as np
from MeshWithSolve import Mesh
from MeshDyn import MeshDyn
from Node import Node
from plot import plotWholeRoom
from plotValMatrix import plotRoom

'''
script to plot the whole apartment
'''

def plotApartment(valRoom1,valRoom2,valRoom3):
    totalX = valRoom1.shape[1]+valRoom2.shape[1]+valRoom3.shape[1]
    mat = np.zeros([valRoom2.shape[0],totalX])
    mat[0:valRoom1.shape[0],0:valRoom1.shape[1]]=valRoom1
    mat[0:valRoom2.shape[0],valRoom1.shape[1]:valRoom2.shape[1]]=valRoom2
    mat[valRoom1.shape[0]:,valRoom1.shape[1]+valRoom2.shape[1]:valRoom1.shape[1]]=valRoom3
    fig = plotRoom(mat)
    return fig