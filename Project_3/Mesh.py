# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016
@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl
from Node import Node,NodeType

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
        try:
            self._dim=len(nodeMatrix),len(nodeMatrix[0])
        except:
            raise Exception('nodeMatrix is not a Matrix!')
    
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

    def getDim(self):
        '''
        Get function for the dimension of the nodeMatrix
        '''
        return self._dim

    def setDim(self,dim):
        '''
        Set function for the dimension (not allowed)
        '''
        raise Exception('You are not allowed to change the dimension!')
    
        
    nodeMatrix=property(getNodeMatrix,setNodeMatrix)      
    roomNbr=property(getRoomNbr,setRoomNbr)
    stepSize=property(getStepsize,setStepsize)
    dim=property(getDim,setDim)
    
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
        
    def getValMatrix(self):
        '''
        Returns a matrix with the temperature in every node
        '''
        valMatrix=zeros(self._dim)
        for i in len(self._dim[0]):
            for j in len(self._dim[1]):
                valMatrix[i,j]=self._nodeMatrix[i,j].getFuncVal()
        return valMatrix
    
    def solveAndStore(self):
        """
        solves and stores the solution into the nodes
        """
        vec=self.solve()
        self.store(vec)
        
    def store(self,vec):
        '''
        stores the values in the vector into the nodes in the nodeMatrix
        '''
        lenVec=len(vec)
        if lenVec!=self.dim[0]*self.dim[1]:
            raise Exception('The vector and the node matrix need to have the same number of elements!')
        for i in range(lenVec):
            #set prevFuncVal=u_k and funcVal=u_{k+1}
            self.nodeMatrix[indexVec2indexMat(i)].setFuncValAndPrevFuncVal(vec[i])

    def indexVec2indexMat(self,indexVec):
        '''
        calculate for the index of the vector the index to the corresponding element
        in the matrix
        '''
        numberOfColumns=self.dim[0]
        row=math.floor(indexVec/numberOfColumns)
        column=indexVec%numberOfColumns
        return row,column
        
    def doRelaxation(self,omega):
        '''
        calculate the new values at the boundary
        relaxValue=omega*u_{k+1}+(1-omega)*u_k
        we store the new value onto u_{k+1}
        '''
        coeff2=1-omega #to speed up the calculation calculate this just once
        for i in len(self.nodeMatrix):
            for j in len(self.nodeMatrix[0]):
                #u_{k+1}=omega*u_{k+1}+(1-omega)*u_k
                self.nodeMatrix[i,j].funcVal=omega*self.nodeMatrix[i,j].funcVal+coeff2*self.nodeMatrix[i,j].prevFuncVal
