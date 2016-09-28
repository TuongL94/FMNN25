import unittest
from OptimizationProblem import OptimizationProblem
from scipy import *
import numpy as np

class TestOptimizationProblem(unittest.TestCase):

    def f(self,x):
        return dot(x,x)
    def g(self,x):
        return 2*x

        
    def setUp(self):
        """
        Set up the optimization problem
        """
        self.optProb=OptimizationProblem(self.f,self.g)
        self.optProb2=OptimizationProblem(self.f)

    def testInit(self):
        """
        Test the init-function
        """
        assert self.optProb.f==self.f
        assert self.optProb.g==self.g
        assert self.optProb.f==self.optProb2.f
        assert self.optProb.g!=self.optProb2.g

    def testApproxG(self):
        """
        Testing the approximation of the gradient by using a value
        """
        x=np.array([1,2,3])
        np.testing.assert_array_almost_equal(self.optProb.g(x),self.optProb2.g(x))

if __name__=='__main__':
    unittest.main()
