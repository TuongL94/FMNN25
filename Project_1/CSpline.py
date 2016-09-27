# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:07:26 2016
@author: Bernhard
"""
from  pylab import *
import matplotlib.pyplot as plt


'''
input:
-u = value of which you want to find the hot interval
-nodes = nodes of the grid you are using
returns the second where u is in it (u\in[u_{index-1},u_index))
'''
def getHotInterval(u,nodes):
    # finds hot interval and returns the index of the right side of the interval.
    # special case if u==u_K
    #iPlusOne = (self.nodes > u). argmax ()
    #if u == self.nodes[-3] and  iPlusOne>= len(self.nodes)-2:
        #iPlusOne -= 1
    #return iPlusOne
    if u==nodes[-1]:
        return (nodes == u). argmax ()
    else:
        return (nodes > u). argmax ()

'''
class for representing a cubic spline (cubic == polDeg=3)
'''
class CSpline:
    _polDeg=3
    '''
    Constructor
    input:
    controlPoints = control points of the CSpline (d)
    nodes = nodes of the grid (u)
    '''
    def __init__(self,controlPoints,nodes,polDeg=3):
        if len(controlPoints) < polDeg:
            raise Exception('Number of control points needs to at least', polDeg)
        if len(nodes) != len(controlPoints)+2:
            raise Exception('Number of nodes needs to be exactly ', len(controlPoints)+2)
        #convert to float
        self._controlPoints = controlPoints.astype(float)
        self._nodes = nodes.astype(float)
        CSpline._polDeg = polDeg

    '''
    get-function of the control points
    returns the controlPoints
    '''
    def getControlPoints(self):
        return self._controlPoints

    controlPoints = property(getControlPoints)

    '''
    get-function of the nodes
    returns the nodes
    '''    
    def getNodes(self):
        return self._nodes

    nodes = property(getNodes)

    '''
    call function of the spline
    you are able to call the function with s(u) (s is an instance of a CSpline)
    input:
    -u = value where you want to evaluate the CSpline
    returns the value of the CSpline at the given point u
    '''    
    def __call__(self,u):
        # find hot interval
        iPlusOne = getHotInterval(u,self.nodes)
        #special case (if u==last possible node)
        if iPlusOne == len(self.nodes)-2 and u == self.nodes[iPlusOne-1]:
            iPlusOne = iPlusOne -1
        # error message when u not in possible interval
        if iPlusOne < 3 or iPlusOne >= len(self.nodes)-2:
            raise Exception('Choose u between', self.nodes[2], self.nodes[len(self.nodes)-3])
        # collect needed control points
        d = array(self._controlPoints[iPlusOne-3:iPlusOne+1])
        # calculate CSpline s(u) by DeBoor-algorithm
        for i in range(0,CSpline._polDeg):
            for k in range(0,CSpline._polDeg-i):
                #calc the denom
                alpha = (self.nodes[iPlusOne+k]-self.nodes[iPlusOne-CSpline._polDeg+k+i])
                if alpha!= 0:
                    alpha = (self.nodes[iPlusOne+k]-u)/alpha
                d[k] = alpha*d[k]+(1-alpha)*d[k+1]
        return d[0]



    '''
    Plot function. The function plots the spline between defined nodes. It also plots the
    control points.
    '''
    def plot(self):
        us = linspace(self.nodes[2],self.nodes[-3],len(self.controlPoints)*10)
        ss = zeros((2,len(us))) #Value of the splines for the inputs us
        for k in range(len(us)):
            ss[:,k] = self.__call__(us[k])
        controlPoints = self.getControlPoints()
        plt.plot(ss[0,:],ss[1,:],controlPoints[:,0],controlPoints[:,1],'ro--')
        plt.show()

    '''
    calculates the basis function to the given index j and the given set of nodes
    input:
        -j = index of the basis function
        -nodes = set of grid points
    returns a basis function - you are evaluate the function at the point by using this
    point as a parameter
    '''
    @classmethod
    def getBasisFunction(cls,j,nodes):
        def basisFunc(u):
            #basis
            basisArr = array((cls._polDeg+1)*[0.])
            #factors
            factors = array([0.,0.])
            # find hot interval
            indexHotInt = getHotInterval(u,nodes)
            indexDiff = indexHotInt - j
            if indexDiff>=0 and indexDiff<=cls._polDeg:
                basisArr[indexDiff] = 1
            else:
                return 0
            for k in range(1,cls._polDeg+1):
                for i in range(j,j+cls._polDeg+1-k):
                    #case out of bounds (-1) (u[-1]=u[0])
                    if i == 0:
                        #calc denoms
                        factors[0] = nodes[i+k-1]-nodes[i]
                        if factors[0]!=0:
                            factors[0] = (u-nodes[i])/factors[0]
                    else:
                        #calc denoms
                        factors[0] = nodes[i+k-1]-nodes[i-1]
                        if factors[0]!=0:
                            factors[0] = (u-nodes[i-1])/factors[0]
                    #case out of bounds (K+1) (u[K+1]=u[k])
                    if i+k == len(nodes):
                        factors[1] = nodes[i+k-1]-nodes[i]
                        if factors[1]!=0:
                            factors[1] = (nodes[i+k-1]-u)/factors[1]
                    else:
                        factors[1] = nodes[i+k] - nodes[i]
                        if factors[1]!=0:
                            factors[1] = (nodes[i+k]-u)/factors[1]
                    basisArr[i-j] = factors[0]*basisArr[i-j]+factors[1]*basisArr[i-j+1]
            return basisArr[0]
        return basisFunc

    '''
    calculates the de Boor Points for some interpolation points
    input:
        -nodes = grid points
        -x = x-values of the interpolation points
        -y = y-values of the interpolation points
    returns the control points which generates the interpolated curve of the x values
    '''    
    @classmethod
    def makeDeBoorPoints(cls,nodes,x,y):
        lenNodes = len(nodes)
        #size of the vector and matrix
        lenSystem = lenNodes-2
        if lenNodes < 3:
            raise Exception("You have to give at least 3 nodes")
        if nodes[0]!=nodes[1] or nodes[1]!=nodes[2]:
            raise Exception("The first 3 nodes needs to have the same value")
        if nodes[-1]!=nodes[-2] or nodes[-2]!=nodes[-3]:
            raise Exception("The last 3 nodes needs to have the same value")
        #calculate the xi's
        xis = array([(nodes[i]+nodes[i+1]+nodes[i+2])/3. for i in range(0,lenSystem)])
        #calculate the matrix with the basisfunctions
        matA = array([array([cls.getBasisFunction(i,nodes)(xis[j]) for i in range(0,lenSystem)]) for j in range(0,lenSystem)])
        matB = [x,y]
        return solve(matA,matB)