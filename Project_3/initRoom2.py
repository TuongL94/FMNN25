# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:38:51 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *
from Node import Node
from MeshWithSolve import Mesh

import pdb

def initRoom2():
    '''
    Initilizing the "second" room. Returns a Mesh instance
    '''
    meshsize=1/20 # Distance between nodes 1/k gives k+1 nodes
    xRoom2=1        #Length of room 2
    yRoom2=2        #width of room 2
    xNodes=round(xRoom2/meshsize+1) # nbr of nodes in x-direction
    yNodes=round(yRoom2/meshsize+1) # nbr of nodes in y-dierction
    matrix=empty((yNodes,xNodes),dtype=Node)    #Create empty array
    #pdb.set_trace()
    ytemp=round(yNodes/2)
     
    '''
    Starting by setting all nodes to inner nodes
    '''
    
    for y in range(yNodes):
        for x in range(xNodes):
            tempNode=Node(x*meshsize,y*meshsize,'inner',15)
            matrix[y,x]=tempNode

    
    '''
    Setting the normal walls and the interfaces (vertical walls)
    '''
    for k in range(round(yNodes/2)): #Half the wall
        #Upperleft normal wall
        matrix[k,0].setNodeType('Dirichlet')
        #Upperright interface
        matrix[k,xNodes-1].setNodeType('Dirichlet')
        #Lowerleft interface
        matrix[k+round(yNodes/2),0].setNodeType('Dirichlet')
        #Lowerright normal wall
        matrix[k+round(yNodes/2),xNodes-1].setNodeType('Dirichlet')
    '''
    Setting the window and heater (horizontal walls)
    '''
    for k in range(xNodes):
        #Upper heater wall
        matrix[0,k].setFuncVal(40)
        matrix[0,k].setPrevFuncVal(40)
        matrix[0,k].setNodeType('Dirichlet')
        #Lower window wall
        matrix[yNodes-1,k].setFuncVal(5)
        matrix[yNodes-1,k].setNodeType('Dirichlet')
        

    
    mesh2=Mesh(matrix,2,meshsize)
            
    return mesh2
    
