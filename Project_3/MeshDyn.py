# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import numpy as np
import pylab as pl
import Node

# imports for the plotting function
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


class MeshDyn():
    """
    class representing the mesh which discretizes the rooms in project 3
    teaser how the class could be designed for arbitrary room contallations    
    """
    
    def __init__(self,nodeMatrix=None,xLength=None,yLength=None,boundary=None,meshsize):
        """
        sets up an instance of the mesh-class
        input parameters: 
            either a complete node matrix
            or the dimensions of the room (length in x- and y-direction): xLength, yLength
            and specifications of the boundaries
            here: only sinple case: one bounday has only one boundary condition
            give array [a,b,c,d], where a, b, c, d can be either 'N' or 'D'
            (Neumann or Dirichlet boundary) 
            a is the left, b the lower, c the right and d the upper wall of the room
            distance between the nodes: meshsize
        """
        if nodeMatrix is None:
            #setup algorithm
            raise Exception('Algorithm missing.')
            self._xLength = xLength
            self._yLength = yLength
            self.numberOfXNodes = self.xLength/self.meshsize+1
            self.numberOfYNodes = self.yLength/self.meshsize+1
        else:
            self.nodeMatrix = nodeMatrix
            self.numberOfXNodes = nodeMatrix.shape[1]
            self.numberOfYNodes = nodeMatrix.shape[0]
            
        if xLength is None:
            if nodeMatrix is None:
                raise Exception('Give either a matrix or the parameter to set up one.')
        else:
            self._xLength = (nodeMatrix.shape[1]-1)*meshsize
            self._yLength = (nodeMatrix.shape[2]-1)*meshsize
        
        self._meshsize = meshsize
        
        # some more input parameter
        # algo to set up the nodeMatrix
        
            # should be part of the init-function
#    def createNodes(self):
#        # create instances of the node-class for the given mesh?
#        # implement actual algorithm
#        """
#        return:
#        """
#        # What do we do if stepsize doesn't devide wdth or length exactly?
#        # calculate the number off needed nodes in x- and y-direction        
#        numberOfXNodes = self._xLength/self._meshsize+1
#        numberOfYNodes = self._yLength/self._meshsize+1
#        # preallocate a matrix to store the nodes in it
#        mesh = np.empty(numberOfYNodes,numberOfXNodes,dtype=object)
#        for i in range(numberOfYNodes):
#            for j in range(numberOfXNodes):
#                mesh[:,:] = Node(self._meshsize*i,self._meshsize*j,'inner')
#        for j in range(numberOfXNodes):
#            mesh[,]
#        return mesh
    
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
        
        # more get-functions for the input parameter
        
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
    
    # more set functions for the other input parameter    
    
    xLength=property(getXLength,setXLength)
    yLength=property(getYLength,setYLength)
    meshsize=property(getMeshsize,setMeshsize) 
    # more properties
    
    def plotRoomPart(self):
        """
        surface plot of the temperature in one roompart
        return: a figure object tha shows the plot
        """
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        X = np.arange(-self.meshsize, self.xLength+self.meshsize, \
        self.meshsize)
        Y = np.arange(-self.meshsize, self.yLength+self.meshsize, self.meshsize)
        X, Y = np.meshgrid(X, Y)
        Z = np.array([[self.nodeMatrix[i,j].funcVal for i in range(self.numberOfYNodes)] \
            for j in range(self.numberOfXNodes)])
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
        # set limits for z-axis
        ax.set_zlim(np.amin(Z)-self.meshsize, np.amax(Z)+self.meshsize)
        # don't know what these two lines are for
        # x.zaxis.set_major_locator(LinearLocator(10))
        # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        # don't know what these two lines are for
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()    
        return fig
    

    def setupSolveMatrixAndRhs(self):
        """
        sets up the matrix and right hand side needed to solve the linear system
        arising from the finite difference discretization of the Laplacian
        return: matrix and right hand side
        """
        # could use the fact, that lapA will be a banded matrix
        # feature for future work
        numberOfNodes = self.numberOfXNodes*self.numberOfYNodes
        #numberOfDirNodes  = 0
        #for i in range(self.numberOfYNodes):
        #    for j in range(numberOfXNodes):
        #        if self.nodeMatrix.nodeType == 'Dirichlet':
        #            numberOfDirNodes = numberOfDirNodes+1                   
        #lapA = np.zeros(numberOfNodes-numberOfDirNodes,numberOfNodes-numberOfDirNodes)
        lapA = np.zeros(numberOfNodes,numberOfNodes)
        #rhs = np.zeros(numberOfNodes-numberOfDirNodes)
        rhs = np.zeros(numberOfNodes)        
        counter = 0
        for i in range(self.numberOfYNodes):
            for j in range(self.numberOfXNodes):
                # what to do when node is a Dirichlet node
                if self.nodeMatrix[i,j].nodeType == 'Dirichlet':
                    # write 1 on the corresponding diagonal position of the solvematrix
                    lapA[counter,counter] = 1
                    #write the prescribed boundary value on the corresponding position
                    # on the right hand side
                    rhs[counter] = self.nodeMatrix[i,j].funcVal
                    counter = counter+1
                # what to do when node is an inner node    
                elif self.nodeMatrix[i,j].nodeType == 'inner':
                    # write -4 on the diagonal
                    lapA[counter,counter] = -4
                    # check the 4 adjacant nodes
                    # [i-1,j]
                    if self.nodeMatrix[i-1,j].nodeType == 'inner':
                        lapA[counter,counter-1] = 1     
                    elif self.nodeMatrix[i-1,j].nodeType == 'Dirichlet':
                        rhs[counter] = rhs[counter]-self.nodeMatrix[i-1,j].funcVal                                
                    else:
                        lapA[counter,counter-1] = 1
                    # [i+1,j]
                    if self.nodeMatrix[i+1,j].nodeType == 'inner':
                        lapA[counter,counter+1] = 1     
                    elif self.nodeMatrix[i+1,j].nodeType == 'Dirichlet':
                        rhs[counter] = rhs[counter]-self.nodeMatrix[i+1,j].funcVal                                
                    else:
                        lapA[counter,counter+1] = 1
                    # [i,j-1]
                    if self.nodeMatrix[i,j-1].nodeType == 'inner':
                        lapA[counter,counter-self.numberOfXNodes] = 1     
                    elif self.nodeMatrix[i,j-1].nodeType == 'Dirichlet':
                        rhs[counter] = rhs[counter]-self.nodeMatrix[i,j-1].funcVal                                 
                    else:
                        lapA[counter,counter-self.numberOfXNodes] = 1
                    # [i,j+1]
                    if self.nodeMatrix[i,j+1].nodeType == 'inner':
                        lapA[counter,counter+self.numberOfXNodes] = 1     
                    elif self.nodeMatrix[i,j+1].nodeType == 'Dirichlet':
                         rhs[counter] = rhs[counter]-self.nodeMatrix[i,j+1].funcVal                               
                    else:
                        lapA[counter,counter+self.numberOfXNodes] = 1
                    counter = counter+1
                # what to do when node is a Neumann node
                else:
                    #write -3 on the diagonal
                    lapA[counter,counter] = -3 
                    # check the three adjacant nodes
                    # find the 'nonexisting' one by catching an index exception?
                    # [i-1,j]
                    try:
                        self.nodeMatrix[i-1,j]
                        if self.nodeMatrix[i-1,j].nodeType == 'inner':
                            lapA[counter,counter-1] = 1                        
                        elif self.nodeMatrix[i-1,j].nodeType == 'Dirichlet':
                            rhs[counter] = rhs[counter]-self.nodeMatrix[i-1,j].funcVal                                
                        else:
                            lapA[counter,counter-1] = 1
                    # set derivative on right hand side
                    except IndexError:
                        rhs[counter] = self.nodeMatrix[i-1,j].deriv
                    # [i+1,j]
                    try:
                        self.nodeMatrix[i+1,j]        
                        if self.nodeMatrix[i+1,j].nodeType == 'inner':
                            lapA[counter,counter+1] = 1     
                        elif self.nodeMatrix[i+1,j].nodeType == 'Dirichlet':
                            rhs[counter] = rhs[counter]-self.nodeMatrix[i+1,j].funcVal                                
                        else:
                            lapA[counter,counter+1] = 1
                    # set derivative on right hand side
                    except IndexError:
                        rhs[counter] = self.nodeMatrix[i+1,j].deriv
                    # [i,j-1]
                    try:
                        self.nodeMatrix[i,j-1]                    
                        if self.nodeMatrix[i,j-1].nodeType == 'inner':
                            lapA[counter,counter-self.numberOfXNodes] = 1     
                        elif self.nodeMatrix[i,j-1].nodeType == 'Dirichlet':
                            rhs[counter] = rhs[counter]-self.nodeMatrix[i,j-1].funcVal                                 
                        else:
                            lapA[counter,counter-self.numberOfXNodes] = 1
                    # set derivative on right hand side
                    except IndexError:
                        rhs[counter] = self.nodeMatrix[i,j-1].deriv
                    # [i,j+1]
                    try:
                        self.nodeMatrix[i,j+1]
                        if self.nodeMatrix[i,j+1].nodeType == 'inner':
                            lapA[counter,counter+self.numberOfXNodes] = 1     
                        elif self.nodeMatrix[i,j+1].nodeType == 'Dirichlet':
                             rhs[counter] = rhs[counter]-self.nodeMatrix[i,j+1].funcVal                               
                        else:
                            lapA[counter,counter+self.numberOfXNodes] = 1
                    # set derivative on right hand side
                    except IndexError:
                        rhs[counter] = self.nodeMatrix[i,j+1].deriv                           
                    counter = counter+1   
        return lapA, rhs
        
    
    def solveMesh(self,lapA,rhs):
        """
        function solving the discretized Laplace-equation for the given mesh
        """
        valVec = sp.linalg.solve(lapA,rhs)
        valMat = valVec.np.reshape(self.numberOfYnodes,self.numberOfXNodes)
        for i in range(self.numberOfYNodes):
            for j in range(self.numberOfXNodes):
                self.nodeMatrix[i,j].funcVal = valMat[i,j]