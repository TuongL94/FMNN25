import unittest
from OptimizationProblem import OptimizationProblem
from QuasiNewton import QuasiNewton, MethodType
from scipy import *
import numpy as np

def f(x):
    return dot(x,x)
def g(x):
    return 2*x
def f2(x):
    return pow(dot(x,x),2)-5*dot(x,x)
def g2(x):
    return 4*dot(x,x)*x-10*x

class TestQuasiNewton(unittest.TestCase):
    def setUp(self):
        """
        Set up the optimization problem
        """
        self.optProb=OptimizationProblem(f,g)
        self.optProbWithoutG=OptimizationProblem(f)
        self.classicalNewton=QuasiNewton(self.optProb,MethodType.CLASSICALNEWTON)
        self.optProb2=OptimizationProblem(f2,g2)
        self.optProbWithoutG2=OptimizationProblem(f2)
        self.optBfgs=QuasiNewton(self.optProb,MethodType.BFGS)
        self.optDfp=QuasiNewton(self.optProb,MethodType.DFP)
        self.optclassNew2=QuasiNewton(self.optProb2,MethodType.CLASSICALNEWTON)
        self.optBfgs2=QuasiNewton(self.optProb2,MethodType.BFGS)
        self.optDfp2=QuasiNewton(self.optProb2,MethodType.DFP)
        
    def testInit(self):
        """
        Test the init-function
        """
        print(self.classicalNewton.getSearchDir)
        print(OptimizationMethods.getSearchDirHessian)
        #don't know how to test it        
        #assert self.classicalNewton.getSearchDir!=self.optBfgs.getSearchDir
        #assert self.classicalNewton.lineSearch!=self.optBfgs.lineSearch
        #assert self.classicalNewton.getSearchDir==self.optclassNew2.getSearchDir

    def testSolve(self):
        """
        Test for the solve function
        """
        tol=1e-5
        kmax=5
        x0=0
        #test with solution
        (sol,fval,k)=self.classicalNewton.solve(x0,tol,kmax)
        self.assertAlmostEqual(sol,x0,tol)
        assert k==0
        #test with "near value"
        x0=10
        (sol,fval,k)=self.classicalNewton.solve(x0,tol,kmax)
        (sol2,fval2,k2)=self.optBfgs2.solve(x0,tol,kmax)
        #print (sol2,fval2,k2)
        print('-')
        (sol3,fval3,k3)=self.optDfp2.solve(x0,tol,kmax)
        #print (sol3,fval3,k3)
        print('-')
        #print (sol,sol2,sol3)
        #print(np.linalg.norm(np.array([0])-sol))
        assert np.linalg.norm(np.array([0])-sol)<tol
        assert k==1
        #test with "near value"
        x0=np.array([1000,10,-1112])
        (sol,fval,k)=self.classicalNewton.solve(x0,tol,kmax)
        #print(np.linalg.norm(np.array([0])-sol))
        assert np.linalg.norm(np.array([0,0,0])-sol)<tol
        assert k<=2
        kmax=5
        (sol1,fval1,k1)=self.optclassNew2.solve(x0,tol,kmax)
        #print (sol1,fval1,k1)
        print('-')
        (sol2,fval2,k2)=self.optBfgs2.solve(x0,tol,kmax)
        print (sol2,fval2,k2)
        print('-')
        (sol3,fval3,k3)=self.optDfp2.solve(x0,tol,kmax)
        print (sol3,fval3,k3)
        print('-')
        #assert sol1==sol2==sol3

if __name__=='__main__':
    unittest.main()
    