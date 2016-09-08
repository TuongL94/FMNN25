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
        i=(nodes>u).argmax()-1 #Find I
        hotInterval=array([controlPoints(i-2),controlPoints(i-1),controlPoints(i),controlPoints(i+1)]) #Necessary controlpoints
        #de Bor algorithm on the control points in the hot interval
        #create function alpha(u,uRight,uLeft)
        
    # function for merging two controlpoints
    def merge(self,controlPoint1,controlPoint2,u):
        uLeft=min(controlPoint1.getuLeft(),controlPoint2.getuLeft())
        #same for uRight
        value=alpha(u,uLeft,uRight)*controlPoint1.value()+(1-alpha(..))*controlPoint2.value() #Getting the value for the new
        #controlPoint
        # Find uLeft,uRight for new controlPoint
        
    def plot(self):
        
    def getBasisFunction(self,nodes,j):

s=CSpline(1,2)
s.__call__(u)
s(u)
print(s._controlPoints)

#Class for the controlpoints
class controlPoint:
    def __init___(self,uLeft,uRight,value) #Probably need more u:s than uLeft and uRight
        self._uLeft=uLeft
        self._uRight=uRight
        self.value=value
    def getuLeft(self)
        return self._uLeft
    # And so on...
    
