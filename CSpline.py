# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:07:26 2016

@author: Group
"""

from  scipy import *
from  pylab import *

#class for representing a cubic spline
class CSpline:
    def __init__(self,controlPoints,nodes,polDeg=3):
        if len(controlPoints) < polDeg:
            raise Exception('Number of control points needs to at least', polDeg)
        if len(nodes) != len(controlPoints)+2:
            raise Exception('Number of nodes needs to be exactly ', len(controlPoints)+2)
        #convert to float
        self._controlPoints=controlPoints.astype(float)
        self._nodes=nodes.astype(float)
        self._polDeg=polDeg
    #get-function of the control points
    def getControlPoints(self):
        return self._controlPoints
    #set-function of the control points
    def setControlPoints(self,controlPoints):
        self._controlPoints=controlPoints
    controlPoints=property(getControlPoints,setControlPoints)
    
    #get-function of the nodes
    def getNodes(self):
        return self._controlPoints
    #set-function of the nodes
    def setNodes(self,controlPoints):
        self._controlPoints=controlPoints
    controlPoints=property(getControlPoints,setControlPoints)
    
    #call function of the spline
    #you are able to call the function with s(u) (s is an instance of a CSpline)   
    def __call__(self,u):
        # find hot interval
        iPlusOne=self.getHotInterval(u)
        # error message when u not in possible interval
        if iPlusOne < 3 or iPlusOne >= len(self._nodes)-2:
            raise Exception('Choose u between', self._nodes[2], self._nodes[len(self._nodes)-3])
        # collect needed controlpoints
        d=array(self._controlPoints[iPlusOne-3:iPlusOne+1])
        # calculate CSpline s(u) by DeBoor-algorithm
        for i in range(0,self._polDeg):
            for k in range(0,self._polDeg-i):
                #calc the denom
                alpha=(self._nodes[iPlusOne+k]-self._nodes[iPlusOne-self._polDeg+k+i])
                if alpha!=0:
                    alpha=(self._nodes[iPlusOne+k]-u)/alpha
                d[k]=alpha*d[k]+(1-alpha)*d[k+1]  
        return d[0]
        
    '''
    returns the second where u is in it (u\in[u_{index-1},u_index))
    '''
    def getHotInterval(self,u):
        # find hot interval
        # special case if u==u_K
        if u==self._nodes[-1]:
            return (self._nodes == u). argmax ()
        else:
            return (self._nodes > u). argmax ()
    #Plot function. The function plots the spline between defined nodes. It also plots the 
    #control points.
    def plot(self):
        us=linspace(self._nodes[2],self._nodes[-3])
        ss=zeros((2,len(us))) #Value of the splines for the inputs us
        print(us)        
        for k in range(len(us)-1):
            ss[:,k]=s(us[k])
        contPoints=self.getControlPoints()
        plot(ss[0,:],ss[1,:])
        scatter(contPoints[:,0],contPoints[:,1])
        
    def getBasisFunction(self,j):
        def basisFunc(u):
            #basis
            basisArr=array((self._polDeg+1)*[0.])
            #factors
            factors=array([0.,0.])
            # find hot interval
            indexHotInt=self.getHotInterval(u)
            indexDiff=indexHotInt-j
            if indexDiff>=0 and indexDiff<=self._polDeg:
                basisArr[indexDiff]=1
            else:
                return 0
            for k in range(1,self._polDeg+1):
                for i in range(j,j+self._polDeg+1-k):
                    #case out of bounds (-1) (u[-1]=u[0])
                    if i==0:
                        #calc denoms
                        factors[0]=self._nodes[i+k-1]-self._nodes[i]
                        if factors[0]!=0:
                            factors[0]=(u-self._nodes[i])/factors[0]
                    else:
                        #calc denoms
                        factors[0]=self._nodes[i+k-1]-self._nodes[i-1]
                        if factors[0]!=0:
                            factors[0]=(u-self._nodes[i-1])/factors[0]
                    #case out of bounds (K+1) (u[K+1]=u[k])
                    if i+k==len(self._nodes):
                        factors[1]=self._nodes[i+k-1]-self._nodes[i]
                        if factors[1]!=0:
                            factors[1]=(self._nodes[i+k-1]-u)/factors[1]
                    else:
                        factors[1]=self._nodes[i+k]-self._nodes[i]
                        if factors[1]!=0:
                            factors[1]=(self._nodes[i+k]-u)/factors[1]
                    basisArr[i-j]=factors[0]*basisArr[i-j]+factors[1]*basisArr[i-j+1]
            return basisArr[0]
        return basisFunc
    #generates the control points which generates the interpolated curve of the x values
    @classmethod
    def makeDeBoorPoints(cls,nodes,x,y):
        lenNodes=len(nodes)
        #size of the vector and matrix
        lenSystem=lenNodes-2
        if lenNodes<3:
            raise Exception("You have to give at least 3 nodes")
        if nodes[0]!=nodes[1] or nodes[1]!=nodes[2]:
            raise Exception("The first 3 nodes needs to have the same value")
        if nodes[-1]!=nodes[-2] or nodes[-2]!=nodes[-3]: 
            raise Exception("The last 3 nodes needs to have the same value")           
        #calculate the xi's
        xis=array([(nodes[i]+nodes[i+1]+nodes[i+2])/3. for i in range(0,lenSystem)])
        print(xis)        
        c=CSpline(array(lenSystem*[0]),nodes)        
        #calculate the matrix with the basisfunctions
        #for i in range(0,lenSystem):
        #    for j in range(0,lenSystem):
        #        a=c.getBasisFunction(i)(xis[j])
        matA=array([array([c.getBasisFunction(i)(xis[j]) for i in range(0,lenSystem)]) for j in range(0,lenSystem)])        
        print(matA)
        return matA
        #todo: matrix last line (0-line???)
        #todo: solve the system
        matB=[x,y]
        #matA*d=matB => solve the system
        return solve(matA,matB)
        
x=array([1,2,3,4,5])
y=array([1,2,3,4,5])
nodes=array([0,0,1,3,3.5,4,4])
s=CSpline(array([[1,2],[3,4],[3,5],[3,6],[4,6]]),nodes)
s.plot()
s.getBasisFunction(3)(4)
u=3.66
#print(s(u))
for i in range(0,5):
    print(s.getBasisFunction(i)(0))
    print(s.getBasisFunction(i)(1))
    print(s.getBasisFunction(i)(2.34))
    print(s.getBasisFunction(i)(3.67))
    print(s.getBasisFunction(i)(4))
    print()
#print(s._controlPoints)
CSpline.makeDeBoorPoints(nodes,x,y)