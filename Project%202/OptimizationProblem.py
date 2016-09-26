# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:23:09 2016
@authors: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
from  scipy import *
from  pylab import *

class OptimizationProblem:
    '''
    class for representing an optimization problem
    '''
    def __init__(f,g=[]):
        '''
        initialize the function f and its derivative g
        if the derivative is not given g is set to the approximation of g
        '''
        _f=f;
        if g==[]:
            _g=__approxG__
        else:            
            _g=g
        
    
    def getF(self):
        '''
        get-function of the function f
        '''
        return self._f
    def setF(self):
        '''
        set-function of the function f (not allowed to use)
        '''
        raise Exception('You are not allowed to change the value of the function f');
    f=property(getF,setF)
    
    def getG(self):
        '''
        get-function of the gradient g
        '''
        return self._g
    def setG(self):
        '''
        set-function of the gradient g (not allowed to use)
        '''
        raise Exception('You are not allowed to change the value of the gradient g');
    g=property(getG,setG)
    
    def __approxG__():
        '''
        calculate an approximation of the gradient out of the function f
        '''    
