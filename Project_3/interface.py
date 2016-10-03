# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:51 2016

@author: Anders
"""

from scipy import *
from pylab import *

class interface:
    '''
    input: an array of nodes
    '''
    def __init__(self,boundary):
        self._boundary=boundary
    
    def getBoundary(self):
        return self._boundary
        
    def setBoundary(self,boundary):
        self._boundary=boundary
    boundary=property(getBoundary,setBoundary)
    

b=rand(1,5)
print(b)
interface1=interface(b)
s=interface1.getBoundary()
print(s)
c=rand(1,5)
interface1.setBoundary(c)
print(c)
print(interface1.getBoundary())