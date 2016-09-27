# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:49:30 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *
from enum import Enum
from OptimizationMethods import OptimizationMethods
#from overloading import overload
import warnings

class MethodType:
    """
    Enum representing a number which is significant for the method
    It also provides an array with the necessary information for the method
    """
    CLASSICALNEWTON='Classical Newton'
    BFGS='BFGS'
    DFP='DFP'

class QuasiNewton(OptimizationMethods):
    """
    Class representing diffenrent versions of Quasi-Newton methods
    """
    def __init__(self,optProb,updateH,isHessian=None,linesearch=None,isWolfePowell=True):
        """
        if isHessian==None: 
            def __init__(self,optProb,methodType):(updateH==methodType)
            is initializing the values with the settings of the type
        initialize the function with an instance of the OptimizationProblem
        class
        what about the other parameter? do we leave them here or not?
        """
        self.optProb=optProb
        if isHessian==None:
            methodInfo={\
                MethodType.BFGS: (super().bfgs,False,super(self.__class__,self).lineSearchExactNewton),\
                MethodType.DFP: (super(self.__class__,self).dfp,False,super(self.__class__,self).lineSearchExactNewton),\
                MethodType.CLASSICALNEWTON: (super(self.__class__,self).finiteDifference,True)}
            self.__init__(optProb,*methodInfo[updateH])
        else:
            self.updateHessian=updateH
            if isHessian:
                self.getSearchDir=super().getSearchDirHessian
            else:
                self.getSearchDir=super().getSearchDirInv
            if linesearch!=None:
                self.linsearch=linesearch
            if isWolfePowell:
                self.lc=super().lcWolfePowell
                self.rc=super().rcWolfePowell
            else:
                self.lc=super().lcGoldstein
                self.rc=super().rcGoldstein

        
        
      #if self._linesearch=exact
          #linesearch()=exactlinesearch()
        
    def solve(self,x0,tol=10^-5,kmax=100):
        #H=... #Initial value))
        # first step always done with dinite difference approximation of Hessian,
        # because for update methods, two initial x-values are needed
        H=super().finiteDifference
        if optProb.g(x0)<tol:
            if super().isPosDef()==False: #Hessian is not positive definite - Error message? only stationary point found?
                warnings.warn("Matrix at the result is not positive definite")
            return (x,f(x))
        sk=super().getSearchDirHessian(self.optProb.g(x0),H)
        alfa=self.linesearch(x0,sk)
        xk=xk+alfa*sk
        xkPrev=x0
        # iterational process starts
        for k in range(kmax):
            H=updateHessian(xk,xkPrev)
            if optProb.g(xk)<tol:
                if super().isPosDef()==False: #Hessian is not positive definite - Error message? only stationary point found?
                    warnings.warn("Matrix at the result is not positive definite")
                return (x,f(x))
            sk=self.getSearchDir(self.optProb.g(xk),H)
            alfa=self.linesearch(xk,sk)
            xkPrev=xk
            xk=xk+alfa*sk
        warnings.warn("Algorithm stopped because it reached the maximum number of iterations")
        return (x,f(x))
