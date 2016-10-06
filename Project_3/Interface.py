# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:51 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *
from MeshWithSolve import Mesh
from Node import Node,NodeType

class Interface:
    '''
    input: an array of nodes
    '''
    def __init__(self,mesh,indices):
        '''
        mesh is an instance of a mesh
        indices is an array with the indizes (tupels) of the interface
        refering to the mesh
        '''
        self._indices=indices
        self._mesh=mesh
    
    def getIndices(self):
        return self._indices
        
    def setIndices(self,indices):
        raise Exception('Your are not allowed to set the value of the border!')
    def getMesh(self):
        return self._mesh
        
    def setMesh(self,indices):
        raise Exception('Your are not allowed to set the value of the mesh!')
    indices=property(getIndices,setIndices)
    mesh=property(getMesh,setMesh)
    
    def setValues(self,values,nodeType):
        '''
        setting the values corresponding to the nodetype and the interface
        values should be an array of the size of indices
        '''
        lenIndices=len(self.indices)
        #print(lenIndices)
        if lenIndices!=len(values):
            #return
            #if length is not the same throw an error
            raise Exception('length of the indices and of the values must be the same!',lenIndices,len(values))
        for i in range(lenIndices):
            self.mesh.grid[self.indices[i]].setBoundaryValue(values[i],nodeType)
    def getValues(self,nodeType):
        '''
        get the values corresponding to the nodetype and the interface
        returns an array with the values (function values or derivative) at the interface
        '''
        lenIndices=len(self.indices)
        if nodeType==NodeType.NEUMANN:
            values=self.calcNormDer()
        elif nodeType==NodeType.DIRICHLET:
            values=array([0]*lenIndices)
            for i in range(lenIndices):
                values[i]=self.mesh.grid[self.indices[i]].funcVal
        return values
    
    def calcNormDer(self):
        '''
        approximate the normal derivative with a difference quotient
        return an array with the normal derivatives of each value of the interface
        '''
        lenIndices=len(self.indices)
        values=array([0]*lenIndices)
        for i in range(lenIndices):
            #different cases (prevIndex==index of the element we use for the difference quotient)
            if self.indices[i][0]==0:
                #case1: row on the top
                prevIndex=(self.indices[i][0]+1,self.indices[i][1])
            elif self.indices[i][0]==self.mesh.y_res:
                #case2: row on the bottom
                prevIndex=(self.indices[i][0]-1,self.indices[i,1])
            elif self.indices[i][1]==0:
                #case3: column left
                prevIndex=(self.indices[i][0],self.indices[i][1]+1)
            elif self.indices[i][1]==self.mesh.x_res:
                #case4: column right
                prevIndex=(self.indices[i][0],self.indices[i][1]-1)
            funcVal=self.mesh.grid[self.indices[i]].funcVal
            #funcValPrev==value of the function at x+stepsize
            funcValPrev=self.mesh.grid[prevIndex[0],prevIndex[1]].prevFuncVal
            print('funcVal')
            print(funcVal)
            print('prev')
            print(funcValPrev)
            values[i]=(funcVal+funcValPrev)/self.mesh.meshsize
        return values
'''
b=rand(1,5)
print(b)
interface1=interface(b)
s=interface1.getindices()
print(s)
c=rand(1,5)
interface1.setindices(c)
print(c)
print(interface1.getindices())
'''
