import unittest
from OptimizationProblem import OptimizationProblem
from OptimizationMethods import OptimizationMethods
from QuasiNewton import QuasiNewton,MethodType
from scipy import *
import numpy as np

def f(self,x):
    return dot(x,x)
def g(self,x):
    return 2*x

class TestQuasiNewton(unittest.TestCase):
    def setUp(self):
        """
        Set up the optimization problem
        """
        self.optProb=OptimizationProblem(f,g)
        self.optProbWithoutG=OptimizationProblem(f)
        self.classicalNewton=QuasiNewton(self.optProb,MethodType.CLASSICALNEWTON)

    def testInit(self):
        """
        Test the init-function
        """
        print(self.classicalNewton.getSearchDir)
        print(OptimizationMethods.getSearchDirHessian)
        #assert self.classicalNewton.getSearchDir==OptimizationMethods.getSearchDirHessian

if __name__=='__main__':
    unittest.main()