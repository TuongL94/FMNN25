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
        #find the hot interval (I=i+1)
        i=(self.controlPoints<u).argmax()
        #define n as the number of control points selected for calc (4=cubic)
        n=4
        #select the corresponding control points
        #because the index for the control points starts at 0 and not -2
        #we need to make a switch in the indizes
        k=i
        d=self.controlPoints[k:k+n]
        #calc alphas and run the recursion
#        alpha=n*[0]
#        for j in range(0,n):
#            if j+i+2>=len(self._nodes):
#                node2=0
#            else:
#                node2=self._nodes[j+i+2]
#            if j+i==0 or j+i>len(self._nodes):
#                node1=0
#            else:
#                node1=self._nodes[j+i-1]
#            #if j+i+2!=len(self._nodes) and j+i!=0:
#            denom=node2-node1
#            if denom!=0:
#                alpha[j]=(node2-u)/denom
        nodes=(n+3)*[0]
        for j in range(0,n+3):
            if j+i>0 and j+i<=len(self._nodes):
                nodes[j]=self._nodes[j+i-1]
        return self.__recursiveDeBoor__(d,nodes)
            
        

    def __recursiveDeBoor__(self,d,nodes):
        n=len(d)
        if n==1:
            return d[0]
        else:
            lenDif=len(nodes)-len(d)
            alpha=n*[0]
            for i in range(0,n-1):
                denom=nodes[i+lenDif]-nodes[i]
                if denom!=0:
                    alpha[i]=(nodes[i+lenDif]-u)/denom
                #manipulate the given d
                if i>0:
                    d[i-1]=alpha[i-1]*d[i-1]+(1-alpha[i])*d[i]
            denom=nodes[n-1+lenDif]-nodes[n-1]
            if denom!=0:
                alpha[n-1]=(nodes[n-1+lenDif]-u)/denom
            d[n-2]==alpha[n-2]*d[n-2]+(1-alpha[n-1])*d[n-1]
            return self.__recursiveDeBoor__(d[:-1],nodes)
    def plot(self):
        return 0
        
def getBasisFunction(self,nodes,j):
    return 0

s=CSpline(array([1,2,3,4]),[0,1])
u=0.5
c=s.__call__(u)
s(u)
print(s.controlPoints)
print(c)