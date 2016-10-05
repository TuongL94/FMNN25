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
    
    def __init__(self,nodeMatrix,roomNbr,stepSize):
        """
        Sets up an instance of the mesh-class
        input parameters: 
            :nodeMatrix: A matrix (array) of Nodes
            :roomNbr: The number of the room
            :stepSize: The distance between two nodes in the node matrix
        """
        self._nodeMatrix=nodeMatrix
        self._roomNbr=roomNbr
        self._stepSize=stepSize
        
    
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
        
    def getStepsize(self):
        '''
        Get function for the step size
        '''
        return self._stepSize
        
    def setStepsize(self,stepsize):
        '''
        Set function for the step size (not allowed)
        '''
        raise Exception('You are not allowed to change the step size!')
        
    def getRoomNbr(self):
        '''
        Get function for the room number
        '''
        return self._roomNbr
        
    def setRoomNbr(self,rNbr):
        '''
        Set function for the room number (not allowed)
        '''
        raise Exception('You are not allowed to change the room number!')
    
        
    nodeMatrix=property(getNodeMatrix,setNodeMatrix)      
    roomNbr=property(getRoomNbr,setRoomNbr)
    stepSize=property(getStepsize,setStepsize)
    
  

