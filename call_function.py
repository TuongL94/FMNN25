# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:31:08 2016

@author: as
"""

from  scipy import *
from  pylab import *

#class for representing a cubic spline
class CSpline:
    def __init__(self,controlPoints,nodes,polDeg=3):
        if len(controlPoints) < polDeg:
            raise Exception('Number of control points needs to at least', polDeg)
        if len(nodes) < len(controlPoints)+2:
            raise Exception('Number of nodes needs to at least', polDeg+2)
        self._controlPoints=controlPoints
        self._nodes=nodes
        self._polDeg=polDeg
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
        # find hot interval
        iPlusOne=(self._nodes > u). argmax ()
        # error message when u not in possible interval
        if iPlusOne < 3 or iPlusOne > len(self._nodes)-2:
            raise Exception('Choose u between', self._nodes[2], self._nodes[len(self._nodes)-2])
        # collect needed controlpoints
        d=array(self._controlPoints[iPlusOne-3:iPlusOne+1])
        # calculate CSpline s(u) by DeBoor-algorithm
        for i in range(self._polDeg-1,-1,-1):
            for k in range(0,i):
                alpha=(self._nodes[iPlusOne+k]-u)/(self._nodes[iPlusOne+k]-self._nodes[iPlusOne-3+k+i])
                d[k]=alpha*d[k]+(1-alpha)*d[k+1]  
        return d[0]
        
        
        
    #def plot(self):
        
    #def getBasisFunction(self,nodes,j):
        
s=CSpline(array([[1,2],[3,4]]),array([0,1,2,5,7]))
u=1.9
print(s(u))

#print(s._controlPoints)