# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:07:26 2016
@author: Bernhard
"""
from  scipy import *
from  pylab import *

#class for representing a cubic spline
class CSpline:
    def __init__(self,controlPoints,nodes):
        self._controlPoints=controlPoints
        self._nodes=nodes
    def getControlPoints(self):
        return self._controlPoints
    def setControlPoints(self,controlPoints):
        self._controlPoints=controlPoints
    #def setControlPointsAtIndex(self,controlPoint,index):
    #    temp=controlPoints
    #    temp[index]=controlPoint
    #    controlPoints=temp
        
    controlPoints=property(getControlPoints,setControlPoints)
    def __call__(self,u):
        
    def plot(self):
        
    def getBasisFunction(self,nodes,j):

s=CSpline(1,2)
s.__call__(u)
s(u)
print(s._controlPoints)