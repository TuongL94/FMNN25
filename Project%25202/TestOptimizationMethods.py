import unittest
from OptimizationProblem import OptimizationProblem
from OptimizationMethods import OptimizationMethods
from scipy import *
import numpy as np

def f(self,x):
    return dot(x,x)
def g(self,x):
    return 2*x
class TestOptimizationMethods(unittest.TestCase):

        
    def setUp(self):
        """
        Set up the optimization problem
        """
        self.optProb=OptimizationProblem(f,g)
        self.optProbWithoutG=OptimizationProblem(f)



if __name__=='__main__':
    unittest.main()