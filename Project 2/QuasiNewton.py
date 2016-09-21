# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:49:30 2016

@author: Anders
"""

from scipy import *
from pylab import *

class QuasiNewton(OptimizationMethods):
    
    def __init__(self,optProb,Happrox,linesearch):
        self._optProb=optProb
        self._Happrox=Happrox
        self._linsearch=linesearch
        
        #f=optProb.f
        #g=optProb.g
    def get...:
        
    def set...:
        
      #if self._linesearch=exact
          #linesearch()=exactlinesearch()
        
    def solve(x0,tol=10^-5,kmax):
        x=x0
        H=... #Initial value
        
        for k in range(kmax):
            if f(x)<tol:
                return x, f(x) #Check for more things!
            
            if HapproxParameter==something
                sk=-H*g(x)
                
            alfa=linesearch()
            x=x+alfa+sk
            H=updateH()