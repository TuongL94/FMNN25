# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016
@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl


class Mesh():
    """
    Class representing the mesh of nodes that constitutes a room
    """
    
    def __init__(self,nodeMatrix):
        """
        Sets up an instance of the mesh-class
        input parameters: 
            :nodeMatrix: A matrix (array) of Nodes
        """
        self._nodeMatrix=nodeMatrix
        
    
    def getNodeMatrix(self):
        '''
        Get function for the nodeMatrix
        '''
        return self._nodeMatrix
    
    def setNodeMatrix(self,nodeMatrix):
        '''
        Set function for the nodeMatrix
        '''
        self._nodeMatrix=nodeMatrix
    
        
    nodeMatrix=property(getNodeMatrix,setNodeMatrix)      
          
    
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

