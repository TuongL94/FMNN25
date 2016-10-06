# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl
import numpy as np
import scipy.linalg as sLin
from Node import *


class Mesh():
    """
    class representing the mesh which discretizes the rooms in project 3
    """
    
    def __init__(self,stepsize, roomNbr, grid):
        """
        sets up an instance of the mesh-class
        input parameters: 
            dimensions of the room (length in x- and y-direction): xLength, yLength
            distance between the nodes: meshsize
        """
        self._xLength = ((grid.shape)[0] - 1) * stepsize
        self._yLength = ((grid.shape)[1] - 1) * stepsize
        self._stepSize = stepsize
        self.roomNbr = roomNbr
        self.grid = grid
        self.x_res = (grid.shape)[0]
        self.y_res = (grid.shape)[1]


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
        
    def getStepsize(self):
        """
        get-function for the meshsize of the mesh 
        return: meshsize
        """
        return self._stepSize
        
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
    meshsize=property(getStepsize,setMeshsize)
    
    def solveMesh(self):
        """
        function solving the discretized Laplace-equation for the given mesh
        return: an array containing the solution
        """
        # Solves for room 1
        if self.roomNbr == 1:
            A = self.__computeCoefficientMatrix__(1)
            f = self.__computeRightSide__(1)
            x = sLin.solve(A,f)
            self.__updateMeshValues__(1,x)
        #  Solves for room 2
        elif self.roomNbr == 2:
            A = self.__computeCoefficientMatrix__(2)
            f = self.__computeRightSide__(2)
            x = sLin.solve(A,f)
            self.__updateMeshValues__(2,x)
        # Solves for room 3
        elif self.roomNbr == 3:
            A = self.__computeCoefficientMatrix__(3)
            f = self.__computeRightSide__(3)
            x = sLin.solve(A,f)
            self.__updateMeshValues__(3,x)


    def __computeCoefficientMatrix__(self, roomNbr):
        A = np.zeros(((self.x_res - 2) * (self.y_res - 2), (self.x_res - 2) * (self.y_res - 2)))
        toeplitzRow = []
        for i in range(0,min(self.x_res - 2,self.y_res - 2)):
            if i == 0:
                    toeplitzRow.extend([-4.0])
            elif i == 1:
                    toeplitzRow.extend([1.0])
            else:
                    toeplitzRow.extend([0.0])
        B = sLin.toeplitz(toeplitzRow,toeplitzRow)
        # Fills the matrix A
        for j in range(0, max(self.x_res - 2, self.y_res - 2)):
            A[j * min(self.x_res - 2 ,self.y_res - 2): j * min(self.x_res - 2 ,self.y_res - 2) + min(self.x_res - 2 ,self.y_res - 2), \
            j * min(self.x_res - 2 ,self.y_res - 2): j * min(self.x_res - 2 ,self.y_res - 2) + min(self.x_res - 2 ,self.y_res - 2)] \
            = B
        A[np.arange((A.shape)[0] - min(self.x_res - 2, self.y_res - 2)), np.arange((A.shape)[0] - min(self.x_res - 2, self.y_res - 2)) + \
                min(self.x_res - 2, self.y_res - 2)] = 1
        A[np.arange((A.shape)[0] - min(self.x_res - 2, self.y_res - 2)) + min(self.x_res - 2, self.y_res - 2), np.arange((A.shape)[0] - \
                min(self.x_res - 2, self.y_res - 2))] = 1

        # Modifies the coefficient matrix A for room 1
        if roomNbr == 1:
            for i in range(0,self.y_res - 2):
                A[i + (i+1) * min(self.x_res - 3, self.y_res - 3)][i + (i+1) * min(self.x_res - 3, self.y_res - 3)] = -3
        # Modifies the coefficient matrix A for room 3
        elif roomNbr == 3:
            for i in range(0,self.y_res - 2):
                A[i + i * min(self.x_res - 3, self.y_res - 3)][i + i * min(self.x_res - 3, self.y_res - 3)] = -3
        A *= 1.0/pow(self._stepSize,2)
        return A


    def __computeRightSide__(self, roomNbr):
        f = np.zeros(((self.x_res - 2) * (self.y_res - 2),1))
        # Assembles the right hand side for room 1
        if roomNbr == 1:
            index = 0
            for i in range(0, self.y_res - 2):
                for j in range(0, self.x_res - 2):
                    if (self.grid[1+i][j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][j]).getFuncVal()
                    elif (self.grid[1+i][j]).getNodeType() == 'Neumann':
                        f[index] += self._stepSize * (self.grid[1+i][j]).getDeriv()
                    if (self.grid[i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[i][1+j]).getFuncVal()
                    elif (self.grid[i][1+j]).getNodeType() == 'Neumann':
                        f[index] += self._stepSize * (self.grid[i][1+j]).getDeriv()
                    if (self.grid[1+i][2+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][2+j]).getFuncVal()
                    elif (self.grid[1+i][2+j]).getNodeType() == 'Neumann':
                        f[index] += self._stepSize * (self.grid[1+i][2+j]).getDeriv()
                    if (self.grid[2+i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[2+i][1+j]).getFuncVal()
                    elif (self.grid[2+i][1+j]).getNodeType() == 'Neumann':
                        f[index] += self._stepSize * (self.grid[2+i][1+j]).getDeriv()
                    index += 1
        # Assembles the right hand side for room 2
        elif roomNbr == 2:
            index = 0
            for i in range(0, self.y_res - 2):
                for j in range(0, self.x_res - 2):
                    # Checks the four neighbourhood of the current node and adds the values for the Dirichlet node to f
                    if (self.grid[1+i][j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][j]).getFuncVal()
                    if (self.grid[i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[i][1+j]).getFuncVal()
                    if (self.grid[1+i][2+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][2+j]).getFuncVal()
                    if (self.grid[2+i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[2+i][1+j]).getFuncVal()
                    index += 1
        # Assembles the right hand side for room 3
        elif roomNbr == 3:
            index = 0
            for i in range(0, self.y_res - 2):
                for j in range(0, self.x_res - 2):
                    if (self.grid[1+i][j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][j]).getFuncVal()
                    elif (self.grid[1+i][j]).getNodeType() == 'Neumann':
                        f[index] -= self._stepSize * (self.grid[1+i][j]).getDeriv()
                    if (self.grid[i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[i][1+j]).getFuncVal()
                    elif (self.grid[i][1+j]).getNodeType() == 'Neumann':
                        f[index] -= self._stepSize * (self.grid[i][1+j]).getDeriv()
                    if (self.grid[1+i][2+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[1+i][2+j]).getFuncVal()
                    elif (self.grid[1+i][2+j]).getNodeType() == 'Neumann':
                        f[index] -= self._stepSize * (self.grid[1+i][2+j]).getDeriv()
                    if (self.grid[2+i][1+j]).getNodeType() == 'Dirichlet':
                        f[index] += (self.grid[2+i][1+j]).getFuncVal()
                    elif (self.grid[2+i][1+j]).getNodeType() == 'Neumann':
                        f[index] -= self._stepSize * (self.grid[2+i][1+j]).getDeriv()
                    index += 1
        f *= -1/pow(self._stepSize,2)
        return f

    def __updateMeshValues__(self, roomNbr, newSolution):
        index = 0
        # Updates the values of the inner nodes
        for i in range(0, self.y_res - 2):
            for j in range(0, self.x_res - 2):
                self.grid[1 + i][1 + j].setFuncVal(newSolution[index])
                index += 1
        # Computes the temperatures at the right boundary and stores them in the corresponding mesh nodes
        if roomNbr == 1:
            for i in range(0,self.y_res - 2):
                self.grid[1+i][self.x_res - 1].setFuncVal(newSolution[self.x_res - 3 + i * min(self.x_res -2, self.y_res - 2)] + self._stepSize * self.grid[1+i][self.x_res - 1].getDeriv())
        # Computes the temperatures at the left boundary and stores them in the corresponding mesh nodes
        elif roomNbr == 3:
            for i in range(0,self.y_res - 2):
                self.grid[1+i][0].setFuncVal(newSolution[i * min(self.x_res -2, self.y_res - 2)] - self._stepSize * self.grid[1+i][0].getDeriv())
                
    def doRelaxation(self,omega):
        '''
        calculate the new values at the boundary
        relaxValue=omega*u_{k+1}+(1-omega)*u_k
        we store the new value onto u_{k+1}
        '''
        coeff2=1-omega #to speed up the calculation calculate this just once
        for i in len(self.grid):
            for j in len(self.grid[0]):
                #u_{k+1}=omega*u_{k+1}+(1-omega)*u_k
                self.grid[i,j].funcVal=omega*self.grid[i,j].funcVal+coeff2*self.grid[i,j].prevFuncVal
