# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:49:30 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""

from scipy import *
from pylab import *

class QuasiNewton(OptimizationMethods):
    """
    Class representing diffenrent versions of Quasi-Newton methods
    """
        def __init__(self,optProb,Happrox,linesearch):
            """
            initialize the finction with an instance of the OptimizationProblem
            class
            what about the other parameter? do we leave them here or not?
            """
        self._optProb=optProb
        self._Happrox=Happrox
        self._linsearch=linesearch
        
        #f=optProb.f
        #g=optProb.g
    def get...:
        """
        Get-function to get information about the currently used instance
        """
        
    def set...:
        """
        """
        
      #if self._linesearch=exact
          #linesearch()=exactlinesearch()
        
    def solve(self,x0,tol=10^-5,kmax):
        xk=x0
        H=... #Initial value
        
        for k in range(kmax):
            if optProb.f(xk)<tol:
                if : #Hessian is positive definite
                    return x, f(x)
                else: #Error message? only stationary point found?
                
            if HapproxParameter==#something
                sk=-H*g(x)
                
            alfa=linesearch()
            xk=xk+alfa*sk
            H=updateH()