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
        self.optMeth=OptimizationMethods()

    def testLineSearchInexact(self):
        """
        Test for the function lineSearchInexact
        """
        #Todo
    
    def testLcWolfePowell(self):
        """
        Test for the function lcWolfePowell
        calculated values for the function f and g (above)
        """
        #x=(-1 -1), s=(1 1)
        alpha0=1
        alphaL=0
        fAlpha0=0
        gAlpha0=0
        fAlphaL=2
        gAlphaL=-2
        rho=0.3
        sigma=0.7
        #check error for rho>=sigma
        self.assertRaises(Exception,self.optMeth.lcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.3,0.3))        
        #check error for rho<0
        self.assertRaises(Exception,self.optMeth.lcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,-0.3,0.3))
        #check error for sigma<0
        self.assertRaises(Exception,self.optMeth.lcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.3,-0.3))
        #check error for rho>0.5
        self.assertRaises(Exception,self.optMeth.lcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.7,0.8))
        #check error for sigma>1
        self.assertRaises(Exception,self.optMeth.lcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.3,1.8))
        #check if lc holds        
        assert self.optMeth.lcWolfePowell(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho,sigma)
        #check if lc does not hold
        #x=(-1 -1), s=(-1 -1)
        gAlpha0=-100
        assert self.optMeth.lcWolfePowell(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho,sigma)==False
        

    def testRcWolfePowell(self):
        """
        Test for the function rcWolfePowell
        calculated values for the function f and g (above)
        """
        #x=(-1 -1), s=(1 1)
        alpha0=1
        alphaL=0
        fAlpha0=0
        gAlpha0=0
        fAlphaL=2
        gAlphaL=-2
        rho=0.3
        #check error for rho<0
        self.assertRaises(Exception,self.optMeth.rcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,-0.3))
        #check error for rho>0.5
        self.assertRaises(Exception,self.optMeth.rcWolfePowell,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.7))
        #check if lc holds        
        assert self.optMeth.rcWolfePowell(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)
        #check if lc does not hold
        #x=(-1 -1), s=(-1 -1)
        gAlphaL=-100
        assert self.optMeth.rcWolfePowell(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)==False


    def testLcGoldstein(self):
        """
        Test for the function lcGoldstein
        calculated values for the function f and g (above)
        """
        #x=(-1 -1), s=(1 1)
        alpha0=1
        alphaL=0
        fAlpha0=0
        gAlpha0=0
        fAlphaL=2
        gAlphaL=-2
        rho=0.3
        #check error for rho<0
        self.assertRaises(Exception,self.optMeth.lcGoldstein,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,-0.3))
        #check error for rho>0.5
        self.assertRaises(Exception,self.optMeth.lcGoldstein,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.7))
        #check if lc holds        
        assert self.optMeth.lcGoldstein(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)
        #check if lc does not hold
        #x=(-1 -1), s=(-1 -1)
        fAlpha0=-100
        assert self.optMeth.lcGoldstein(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)==False

    def testRcGoldstein(self):
        """
        Test for the function rcGoldstein
        calculated values for the function f and g (above)
        """
        #x=(-1 -1), s=(1 1)
        alpha0=1
        alphaL=0
        fAlpha0=0
        gAlpha0=0
        fAlphaL=2
        gAlphaL=-2
        rho=0.3
        #check error for rho<0
        self.assertRaises(Exception,self.optMeth.rcGoldstein,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,-0.3))
        #check error for rho>0.5
        self.assertRaises(Exception,self.optMeth.rcGoldstein,(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,0.7))
        #check if lc holds        
        assert self.optMeth.rcGoldstein(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)
        #check if lc does not hold
        #x=(-1 -1), s=(-1 -1)
        gAlphaL=-100
        assert self.optMeth.rcGoldstein(alpha0,alphaL,fAlpha0,gAlpha0,fAlphaL,gAlphaL,rho)==False

    def testGetSearchDirHessian(self):
        """
        Test for the function getSearchDirHessian
        calculated values for the function f and g (above)
        the given point is x=[1 1]. this means H=[[2 0];[0 2]] and g=[2 2]
        """
        g=np.array([2,2])
        H=np.array([np.array([2,0]),np.array([0,2])])
        #solution is (-1, -1)
        d=np.array([-1,-1])
        s=self.optMeth.getSearchDirHessian(g,H)
        assert (s==d).all()

    def testGetSearchDirInv(self):
        """
        Test for the function getSearchDirInv
        calculated values for the function f and g (above)
        the given point is x=[1 1]. this means H=[[2 0];[0 2]] and g=[2 2]
        because we use the Inv-Method we use the inverse of H which is easy to
        calculate
        """
        g=np.array([2,2])
        HInv=np.array([np.array([0.5,0]),np.array([0,0.5])])
        #solution is (-1, -1)
        d=np.array([-1,-1])
        s=self.optMeth.getSearchDirInv(g,HInv)
        assert (s==d).all()
        
    def testLineSearchExactSteepestDesent(self):
        """
        Test for the linesearch applying the steepest descent method
        
        """
        # input arguments
        self.optMeth.lineSearchExactSteepestDesent()
        assert 
        
    def testLineSearchExactNewton(self):
        """
        Test for the linesearch applying the classical Newton method
        
        """
        # input arguments
        self.optMeth.lineSearchExactNewton()
        assert 

   def testfiniteDifference(self):
        """
        Test for the linesearch applying the steepest descent method
        
        """
        # input arguments
        self.optMeth.finiteDifference()
        assert 



if __name__=='__main__':
    unittest.main()