# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import numpy as np
import pylab as pl
import Node


class Mesh():
    """
    class representing the mesh which discretizes the rooms in project 3
    """
    
    def __init__(self,xLength,yLength,meshsize):
        """
        sets up an instance of the mesh-class
        input parameters: 
            dimensions of the room (length in x- and y-direction): xLength, yLength
            distance between the nodes: meshsize
        """
        self._xLength = xLength
        self._yLength = yLength
        self._meshsize = meshsize
        
    
    def getXLength(self):
        """
        get-function for the length of the mesh in x-direction
        return: x-length of the mesh
        """
        return self._xLength
        
    def getYLength(self):
        """
        get-function for the length of the mesh in y-direction
        return: y-length of the mesh
        """
        return self._yLength
        
    def getMeshsize(self):
        """
        get-function for the meshsize of the mesh 
        return: meshsize
        """
        return self._meshsize
        
    def setXLength(self,xLength):
        """
        set-function for the x-length (not allowed to use)
        """
        raise Exception('You are not allowed to change the dimensions of the mesh!')
        
    def setYLength(self,yLength):
        """
        set-function for the y-length (not allowed to use)
        """
        raise Exception('You are not allowed to change the dimensions of the mesh!')

    def setMeshsize(self,meshsize):
        """
        set-function for the meshsize (not allowed to use)
        """
        raise Exception('You are not allowed to change the meshsize!')
    
    xLength=property(getXLength,setXLength)
    yLength=property(getYLength,setYLength)
    meshsize=property(getMeshsize,setMeshsize)       
        
    def createNodes(self):
        # create instances of the node-class for the given mesh?
        # implement actual algorithm
        """
        return:
        """
        # What do we do if stepsize doesn't devide wdth or length exactly?
        # calculate the number off needed nodes in x- and y-direction        
        numberOfXNodes = self._xLength/self._meshsize+1
        numberOfYNodes = self._yLength/self._meshsize+1
        # preallocate a matrix to store the nodes in it
        mesh = np.empty(numberOfYNodes,numberOfXNodes,dtype=object)
        for i in range(numberOfYNodes):
            for j in range(numberOfXNodes):
                mesh[:,:] = Node(self._meshsize*i,self._meshsize*j,'inner')
        for j in range(numberOfXNodes):
            mesh[,]
        return mesh
    
    #def solveMesh(self,...):
        # check which input arguments are missing
        # implement the actual function
        """
        function solving the discretized Laplace-equation for the given mesh
        return: data that can be used for a plot
        """
        # repeatedly calls solveNode to solve the linear system arrising from 
        # discretized Laplace equation at every node?
        # ordering the data in a sensible output type
        #return
        
    #def solveNode(self,...) :
        # check which input arguments are missing
        # implement the actual function
        """
        function solving the discretized Laplace-equation at a single node
        assigns the calculated function value of the node to the the property 
        _funVal of the node
        return: something the solveMesh function can work with
        """
        #return   