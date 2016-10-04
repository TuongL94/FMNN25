# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl

class Node():
    """
    Class repesenting the nodes of the mesh created in the mesh-class
    """
    
    def __init__(self,xCoord,yCoord,nodeType):
        """
        sets up an instance of the node-class
        input parameters:
            coordinates of the node: xCoord, yCoord
            type of the node ->
            three different types ar possible, depending on where the node lies
            within the mesh:
                Neumann, when part of a Neumann boundary
                Dirichlet, when part of a Dirichlet boundary
                inner, when not part of a bounday
        the function value of the temperature distribution at the node is
        initally set do an empty array
        """
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._nodeType = nodeType
        # three types of nodes possible:
        # Neumann, when part of a Neumann boundary
        # Dirichlet, when part of a Dirichlet boundary
        # inner, when not part of a bounday
        self._funcVal = sp.array([])
        
    def getXCoord(self):
        """
        get-function for the x-coordinate of the node 
        return: x-coordinate
        """
        return self._xCoord
        
    def getYCoord(self):
        """
        get-function for the y-coordinate of the node 
        return: y-coordinate
        """
        return self._yCoord
    
    def getNodeType(self):
        """
        get-function for the type of the node
        return: nodetype
        """
        return self._nodeType
        
        
    def setXCoord(self,xCoord):
        """
        set-function for the x-coordinate (not allowed to use)
        """
        raise Exception('You are not allowed to change the coordinates of a node!')
        
    def setYCoord(self,yCoord):
        """
        set-function for the y-coordinate (not allowed to use)
        """
        raise Exception('You are not allowed to change the coordinates of a node!')
        
    def setNodeType(self,nodeType):
        """
        set-function for the nodetype
        """
        self._nodeType = nodeType
        # raise exception if nodetype not one of the three expected types?        
        
    xCoord=property(getXCoord,setXCoord)
    yCoord=property(getYCoord,setYCoord)
    nodeType=property(getNodeType,setNodeType)

    
        
    def funcVal(self,funcVal):
        """
        assigns the function value of the temperature distribution at the node
        return: function value at the node
        """
        self._funcVal = funcVal
        return funcVal
        
        
node1 = Node(1,2,'Neumann')
       
   
       