import unittest
from OptimizationProblem import OptimizationProblem
from QuasiNewton import QuasiNewton, MethodType
import scipy as sp
from chebyquad_problem import *
import numpy as np

def f(x):
    return dot(x,x)
def g(x):
    return 2*x
def f2(x):
    return pow(dot(x,x),2)-5*dot(x,x)
def g2(x):
    return 4*dot(x,x)*x-10*x
def rosf(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
def rosg(x):
    return 2*np.array([200*(x[1]-x[0]**2)*(-x[0])-(1-x[0]),100*(x[1]-x[0]**2)])

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

    def testRosenBrockClassic(self):
        """
        Optimzes the Rosenbrock function with the classical Newton method
        """
        prob = OptimizationProblem(rosf,rosg)
        solver = QuasiNewton(prob,MethodType.CLASSICALNEWTON)
        tol=1e-5
        kmax=50
        x0 = transpose(np.array([0.0,0.0]))
        (solution,fval,k) = solver.solve(x0,tol,kmax)
        self.assertAlmostEqual(fval,0)
        np.testing.assert_allclose(solution,array([1,1]),0,1e-5)
        #print(solution)    

    def testRosenBrockLineSearch(self):
        """
        Optimizes the Rosenbrock function with a Newton method that applies a 
        linesearch using a steepest descent algorithm
        """
        prob = OptimizationProblem(rosf,rosg)
        solver = QuasiNewton(prob,MethodType.ClassicalNewtonExactLineSteepest)
        tol=1e-5
        kmax=50
        x0 = transpose(np.array([0.0,0.0]))
        (solution,fval,k) = solver.solve(x0,tol,kmax)
        self.assertAlmostEqual(fval,0)
        np.testing.assert_allclose(solution,array([1,1]),0,1e-5)
        #print(solution)
        
    def testRosenBrockNewtonVsLineSearch(self):
        """
        Tests if the two versions of the Algorithm come to the same optimum
        """
        prob = OptimizationProblem(rosf,rosg)
        solver1 = QuasiNewton(prob,MethodType.CLASSICALNEWTON)
        solver2 = QuasiNewton(prob,MethodType.ClassicalNewtonExactLineSteepest)
        tol=1e-5
        kmax=50
        x0 = transpose(np.array([0.0,0.0]))
        (solution1,fval1,k1) = solver1.solve(x0,tol,kmax)
        (solution2,fval2,k2) = solver2.solve(x0,tol,kmax)
        self.assertAlmostEqual(fval1,fval2)
        np.testing.assert_allclose(solution1,solution2,0,1e-5)
        #print(solution)
        
    def testRosenBrockLineSearchInexact(self):
        """
        Optimizes the Rosenbrock function with a Newton method that applies inexact 
        linesearch
        """
        prob = OptimizationProblem(rosf,rosg)
        solver = QuasiNewton(prob,MethodType.ClassicalNewtonInexactLine)
        tol=1e-5
        kmax=50
        x0 = transpose(np.array([0.0,0.0]))
        (solution,fval,k) = solver.solve(x0,tol,kmax)
        self.assertAlmostEqual(fval,0)
        np.testing.assert_allclose(solution,array([1,1]),0,1e-5)
        #print(solution)
        
    def testChebyquad(self):
        #testing the chebyshev polynomial
        x4=np.array([0]*4)
        optProb=OptimizationProblem(chebyquad_fcn,gradchebyquad)
        newtonLinesearchSteepest=QuasiNewton(optProb,MethodType.ClassicalNewtonExactLineSteepest)
        bfgs=QuasiNewton(optProb,MethodType.ClassicalNewtonExactLineSteepest)
        x8=np.array([0]*8)
        x11=np.array([0]*11)
        #calculate with exact linesearch
        newton4=newtonLinesearchSteepest.solve(x4)[0]
        newton8=newtonLinesearchSteepest.solve(x8)[0]
        newton11=newtonLinesearchSteepest.solve(x11)[0]
        #calculate with provided bfgs
        scipy4=sp.optimize.fmin_bfgs(chebyquad,x4)
        scipy8=sp.optimize.fmin_bfgs(chebyquad,x8)
        scipy11=sp.optimize.fmin_bfgs(chebyquad,x11)
        #calculate with our bfgs
        bfgs4=bfgs.solve(x4)[0]
        bfgs8=bfgs.solve(x8)[0]
        bfgs11=bfgs.solve(x11)[0]
        print("Cheby-Newton:")
        print(newton4)
        print(newton8)
        print(newton11)
        print("Cheby-Scipy:")
        print(scipy4)
        print(scipy8)
        print(scipy11)
        print("Cheby-BFGS:")
        print(bfgs4)
        print(bfgs8)
        print(bfgs11)
if __name__=='__main__':
    unittest.main()
    
