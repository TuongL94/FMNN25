# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:21:40 2016

@author: Anders
"""

from scipy import *
from pylab import *

def goodBroyden(x1,x0,g1,g0,H0):
    '''
    Updates the inverse of the Hessian H0 to H1 by the "Good Broyden" method. The input
    variables x1 and x0 are the current and previous vectors where the 
    objective function is evaluated. The variables g1 and g0 are the corresponding
    gradients. H0 is the previous inverse Hessian.
    The input variables have to be row vectors.
    '''
    #Optionally the gradient is calculated inside i.e. g1=gradient(f(x1))
    delta=x1-x0
    gamma=g1-g0
    u=delta-dot(H0,gamma)
    a=1/(dot(transpose(u),gamma))
    H1=H0+a*dot(u,transpose(u))  
    return H1
    

 

    
    