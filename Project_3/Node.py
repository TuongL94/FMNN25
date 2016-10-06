# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:25:36 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""


import scipy as sp
import pylab as pl

class NodeType():
    '''
    class for the names of the types
    '''
    INNER='inner'
    NEUMANN='Neumann'
    DIRICHLET='Dirichlet'

class Node():
    """
    Class repesenting the nodes of the mesh created in the mesh-class
    """
    
    def __init__(self,xCoord,yCoord,nodeType,funcVal):
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
        :funcVal: The initial temperature at the node
        
        """
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._nodeType = nodeType
        self._funcVal=funcVal
        self._prevFuncVal=funcVal #The previous temperature at the node is set to current
        self._deriv=0           #The normal derivative in the node is initially set to 0
        # three types of nodes possible:
        # Neumann, when part of a Neumann boundary
        # Dirichlet, when part of a Dirichlet boundary
        # inner, when not part of a bounday
        #self._funcVal = sp.array([])
        
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
        
    def getFuncVal(self):
        '''
        Get function for the temperature
        '''
        return self._funcVal
        
    def getPrevFuncVal(self):
        '''
        Get function for the previous temperature
        '''
        return self._prevFuncVal
        
    def getDeriv(self):
        '''
        Get function for the derivative
        '''
        return self._deriv
        
        
    def setXCoord(self,xCoord):
        """
        set-function for the x-coordinate
        """
        self._xCoord=xCoord
        
    def setYCoord(self,yCoord):
        """
        set-function for the y-coordinate 
        """
        self._yCoord=yCoord
        
    def setNodeType(self,nodeType):
        """
        set-function for the nodetype
        """
        self._nodeType = nodeType
        # raise exception if nodetype not one of the three expected types? 
        
    def setFuncVal(self,funcVal):
        '''
        Set function for the temperature
        '''
        self._funcVal=funcVal
    def setFuncAndPrevFuncVal(self,funcVal):
        '''
        Set function for the prev temperature to the temperature at the moment
        furthermore set the function value for the temperature with funcVal
        '''
        #set actual value to previous value
        self._prevFuncVal=self._funcVal
        self._funcVal=funcVal
        
    def setPrevFuncVal(self,prevFuncVal):
        '''
        Set function for the previous temperature
        '''
        self._prevFuncVal=prevFuncVal
        
    def setDeriv(self,deriv):
        '''
        Set function for the derivative
        '''
        self._deriv=deriv
        
    def setBoundaryValue(self,value,nodeType):
        '''
        Set the boundary value for the given type (Neumann or Dirichlet)
        '''
        self.nodeType=nodeType
        if nodeType==NodeType.DIRICHLET:#Dirichlet
            self.funcVal=value
        elif nodeType==NodeType.NEUMANN:#Neumann
            self.deriv=value
    def getBoundaryValue(self,nodeType):
        '''
        Get the boundary value for the given type (Neumann or Dirichlet)
        '''
        self.nodeType=nodeType
        if nodeType==NodeType.DIRICHLET:#Dirichlet
            return self.funcVal
        elif nodeType==NodeType.NEUMANN:#Neumann
            return self.deriv

    xCoord=property(getXCoord,setXCoord)
    yCoord=property(getYCoord,setYCoord)
    nodeType=property(getNodeType,setNodeType)
    funcVal=property(getFuncVal,setFuncVal)
    prevFuncVal=property(getPrevFuncVal,setPrevFuncVal)
    deriv=property(getDeriv,setDeriv)
