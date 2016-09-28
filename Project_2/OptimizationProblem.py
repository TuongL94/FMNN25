# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:23:09 2016
@authors: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
from  scipy import *
from  pylab import *
import numpy as np

class OptimizationProblem:
    """
    class for representing an optimization problem
    """
    def __init__(self,f,g=None):
        """
        initialize the function f and its derivative g
        if the derivative is not given g is set to the approximation of g
        """
        self._f=f;
        if g==None:
            self._g=self.__approxG__
        else:            
            self._g=g
        
    
    def getF(self):
        """
        get-function of the function f
        """
        return self._f
    def setF(self,f):
        """
        set-function of the function f (not allowed to use)
        """
        raise Exception('You are not allowed to change the value of the function f');
    f=property(getF,setF)
    
    def getG(self):
        """
        get-function of the gradient g
        """
        return self._g
    def setG(self,g):
        """
        set-function of the gradient g (not allowed to use)
        """
        raise Exception('You are not allowed to change the value of the gradient g');
    g=property(getG,setG)
    
    def __approxG__(self,x):
        """
        calculate an approximation of the gradient out of the function f
        (central difference)
        """
        return np.array([(self.f(x+0.5e-5*np.eye(1,len(x),i)[0])-self.f(x-0.5e-5*np.eye(1,len(x),i)[0]))/1e-5\
        for i in range(len(x))])
