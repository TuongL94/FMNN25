# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:46:49 2016

@author: Anders
"""

from scipy import *
from pylab import *
from Node import Node


def initFinalTestRoom():

    '''
    Initilizing a expecteed final test room where all boundaries are Dirichlet and with
    same temperature.
    '''
    meshsize=1/20 # Distance between nodes 1/k gives k+1 nodes
    xRoom1=1        #Length of room 1
    yRoom1=1        #width of room 1
    xNodes=round(xRoom1/meshsize+1) # nbr of nodes in x-direction
    yNodes=round(yRoom1/meshsize+1) # nbr of nodes in y-dierction
    matrix=empty((yNodes,xNodes),dtype=Node)    #Create empty array
           

    '''
    Starting by setting all nodes to inner nodes and temperature 10
    '''
    
    for y in range(yNodes):
        for x in range(xNodes):
            tempNode=Node(x*meshsize,y*meshsize,'inner',10)
            matrix[y,x]=tempNode

    
    '''
    Setting the vertical walls to Dirichlet
    '''
    for k in range(yNodes):

        matrix[k,0].setNodeType('Dirichlet')
        matrix[k,xNodes-1].setNodeType('Dirichlet')
        
    '''
    Setting horizontal walls to Dirichlet
    '''
    for k in range(xNodes):
        matrix[0,k].setNodeType('Dirichlet')
        matrix[yNodes-1,k].setNodeType('Dirichlet')

    
            
    return matrix