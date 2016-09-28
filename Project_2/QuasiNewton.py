# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:49:30 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *
from enum import Enum
from OptimizationProblem import OptimizationProblem
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
                MethodType.BFGS: (super().bfgs,False,super().lineSearchExactNewton),\
                MethodType.DFP: (super().dfp,False,super().lineSearchExactNewton),\
                MethodType.CLASSICALNEWTON: (super().finiteDifference,True)}
            self.__init__(optProb,*methodInfo[updateH])
        else:
            self.updateHessian=updateH
            if isHessian:
                self.getSearchDir=super().getSearchDirHessian
            else:
                self.getSearchDir=super().getSearchDirInv
            if linesearch!=None:
                self.lineSearch=linesearch
            if isWolfePowell:
                self.lc=super().lcWolfePowell
                self.rc=super().rcWolfePowell
            else:
                self.lc=super().lcGoldstein
                self.rc=super().rcGoldstein

        
        
      #if self._linesearch=exact
          #linesearch()=exactlinesearch()
        
    def solve(self,x0,tol=1e-5,kmax=100):
        #H=... #Initial value))
        # first step always done with dinite difference approximation of Hessian,
        # because for update methods, two initial x-values are needed
        # put it into an array (if it's not already)
        
        #do one finite difference step (for the update formulas we need two iteration points)
        H=super().finiteDifference(x0)
        if np.linalg.norm(self.optProb.g(x0))<tol:
            if super().isPosDef(H)==False:
                warnings.warn("Matrix at the result is not positive definite")
            return (x0,self.optProb.f(x0),0)
        sk=super().getSearchDirHessian(self.optProb.g(x0),H)
        alpha=self.lineSearch(x0,sk)
        xk=x0+alpha*sk
        xkPrev=x0
        # iterational process starts
        for k in range(1,kmax):
            if k==1:
                #differ between array and scalar
                try:
                    H=self.updateHessian(xk,xkPrev,self.optProb.g(xk),self.optProb.g(xkPrev),np.eye(len(x0)))
                except TypeError:
                    H=self.updateHessian(xk,xkPrev,self.optProb.g(xk),self.optProb.g(xkPrev),1)
                #case if we don't have any matrix H for the update formulas
            else:
                H=self.updateHessian(xk,xkPrev,self.optProb.g(xk),self.optProb.g(xkPrev),H)
            if np.linalg.norm(self.optProb.g(xk))<tol:
                if super().isPosDef(H)==False: #Hessian is not positive definite - Error message? only stationary point found?
                    warnings.warn("Matrix at the result is not positive definite")
                return (xk,self.optProb.f(xk),k)
            sk=self.getSearchDir(self.optProb.g(xk),H)
            alpha=self.lineSearch(xk,sk)
            xkPrev=xk
            xk=xk+alpha*sk
        warnings.warn("Algorithm stopped because it reached the maximum number of iterations")
        return (xk,self.optProb.f(xk),kmax)
