# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:59:02 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from Node import Node
from scipy import *
from pylab import *


def initTestRoom():

    '''
    Initilizing a test room where all boundaries are Dirichlet and with
    same temperature.
    '''
    meshsize=1/20 # Distance between nodes 1/k gives k+1 nodes
    xRoom1=1        #Length of room 1
    yRoom1=1        #width of room 1
    xNodes=round(xRoom1/meshsize+1) # nbr of nodes in x-direction
    yNodes=round(yRoom1/meshsize+1) # nbr of nodes in y-dierction
    matrix=empty((yNodes,xNodes),dtype=Node)    #Create empty array
           

    '''
    Starting by setting all nodes to inner nodes and temperature 0
    '''
    
    for y in range(yNodes):
        for x in range(xNodes):
            tempNode=Node(x*meshsize,y*meshsize,'inner',0)
            matrix[y,x]=tempNode

    
    '''
    Setting the vertical walls to temperature 10 and Dirichlet
    '''
    for k in range(yNodes):
        matrix[k,0].setFuncVal(10)
        matrix[k,0].setNodeType('Dirichlet')
        matrix[k,xNodes-1].setFuncVal(10)
        matrix[k,xNodes-1].setNodeType('Dirichlet')
        
    '''
    Setting horizontal walls to temperature 10 and Dirichlet
    '''
    for k in range(xNodes):
        matrix[0,k].setNodeType('Dirichlet')
        matrix[0,k].setFuncVal(10)
        matrix[yNodes-1,k].setNodeType('Dirichlet')
        matrix[yNodes-1,k].setFuncVal(10)

            
    return matrix

