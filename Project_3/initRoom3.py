# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:13:56 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *

def initRoom3():
    #pdb.set_trace()
    '''
    Initilizing the "third" room
    '''
    meshsize=1/20 # Distance between nodes 1/k gives k+1 nodes
    xRoom3=1        #Length of room 3
    yRoom3=1        #width of room 3
    xNodes=round(xRoom3/meshsize+1) # nbr of nodes in x-direction
    yNodes=round(yRoom3/meshsize+1) # nbr of nodes in y-dierction
    matrix=empty((yNodes,xNodes),dtype=Node)    #Create empty array
           
    '''
    Starting by setting all nodes to inner nodes and temperature 15
    '''
    
    for y in range(yNodes):
        #pdb.set_trace()
        for x in range(xNodes):
            tempNode=Node(x*meshsize,y*meshsize,'inner',15)
            matrix[y,x]=tempNode

    
    '''
    Setting the heater wall and the interface
    '''
    for k in range(yNodes):
        matrix[k,xNodes-1].setFuncVal(40)
        matrix[k,xNodes-1].setNodeType('Dirichlet')
        matrix[k,0].setNodeType('Dirichlet')
        
    '''
    Setting the normal walls
    '''
    for k in range(xNodes):
        matrix[0,k].setFuncVal(15)
        matrix[0,k].setNodeType('Dirichlet')
        matrix[yNodes-1,k].setFuncVal(15)
        matrix[yNodes-1,k].setNodeType('Dirichlet')
        

    '''
    Creating an instance of a Mesh (room 3)
    '''
    mesh3=Mesh(matrix) 
    #This is how I would like to create a mesh object.

            
    return matrix
    
M3=initRoom3()