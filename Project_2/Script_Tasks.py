# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:29:13 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
from  scipy import *
from  pylab import *
import timeit
from OptimizationProblem import OptimizationProblem
from QuasiNewton import QuasiNewton, MethodType
from OptimizationMethods import OptimizationMethods

"""
define the Rosenbrock function and its gradient
"""

def rosf(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
    
def rosg(x):
    return 2*array([200*(x[1]-x[0]**2)*(-x[0])-(1-x[0]),100*(x[1]-x[0]**2)])

x0 = array([4,5])
    
"""
make an instance of the class OptimizationProblem, which consists of the
Rosenbrock function and its gradient
"""    
rose = OptimizationProblem(rosf,rosg)

"""
create an instance of the class QuasiNewton
The instance represents the classical Newton Method
"""
claNew = QuasiNewton(rose,MethodType.CLASSICALNEWTON)
BFGSNew = QuasiNewton(rose,'BFGS',linesearch=OptimizationMethods.lineSearchExactNewton)

(x1,f1,k1) = claNew.solve(x0)
(x2,f2,k2) = BFGSNew.solve(x0)
print(x1,f1,k1)
print(x2,f2,k2)
#t = timeit.Timer(claNew.solve(x0))
#t.timeit
