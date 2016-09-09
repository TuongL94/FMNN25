# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:31:08 2016

@author: as
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
    
    def __call__(self,controlPoints,nodes):
        # find hot interval
        IPlusOne=(nodes > self). argmax ()
        # error message when u not at right place?
  ###### change for 2- or n-dimensional points d!!!      
        # collect needed controlpoints
        d=array(controlPoints[IPlusOne-3:IPlusOne+1])
        # calculate CSpline s(u) by DeBoor-algorithm
        for i in range(2,-1,-1):
            for k in range(0,i):
                alpha=(nodes[IPlusOne+k]-self)/(nodes[IPlusOne+k]-nodes[IPlusOne-3+k+i])
                d[k]=alpha*d[k]+(1-alpha)*d[k+1]  
        s=d[0]
        return s
        
        
        
    #def plot(self):
        
    #def getBasisFunction(self,nodes,j):

s=CSpline(1,2)
s.__call__(u)
s(u)
print(s._controlPoints)