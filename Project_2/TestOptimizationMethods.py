import unittest
from OptimizationProblem import OptimizationProblem
from OptimizationMethods import OptimizationMethods
from QuasiNewton import QuasiNewton,MethodType
from scipy import *
import numpy as np

def f(x):
    return dot(x,x)
def g(x):
    return 2*x
#def h(self,x):
#    return 2*eye(len(x))
def f2(x):
    return pow(dot(x,x),2)-5*dot(x,x)
def g2(x):
    return 4*dot(x,x)*x-10*x
class TestOptimizationMethods(unittest.TestCase):

        
    def setUp(self):
        """
        Set up the optimization problem
        """
        self.optProb=OptimizationProblem(f,g)
        self.optProbWithoutG=OptimizationProblem(f)
        self.optMeth=QuasiNewton(self.optProb,MethodType.CLASSICALNEWTON)
        self.optProb2=OptimizationProblem(f2,g2)
        self.optProbWithoutG2=OptimizationProblem(f2)
        self.optMeth2=QuasiNewton(self.optProb2,MethodType.CLASSICALNEWTON)

    def testLineSearchInexact(self):
        """
        Test for the function lineSearchInexact
        """
        #case 'do nothing'
        x=np.array([-1.,-1.])
        s=np.array([1.,1.])
        alpha0=0.5
        (alpha,falpha)=self.optMeth.lineSearchInexact(x,s,alpha0)
        print(alpha)
        self.assertAlmostEqual(alpha,0.5)
        #case rc and lc is not fulfilled (jumping around)
        x=np.array([0,0])
        s=np.array([1.,0])
        alpha0=10
        (alpha,falpha)=self.optMeth2.lineSearchInexact(x,s,alpha0)
        self.assertAlmostEqual(alpha,1.4875137) #calculated value
        #one should do more testing!
    
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
        xk = 2
        sk = -4
        alpha = self.optMeth.lineSearchExactSteepestDesent(xk,sk)
        self.assertAlmostEqual(alpha,0,places=5) 
        
#    def testLineSearchExactNewton(self):
#        """
#        Test for the linesearch applying the classical Newton method
#        
#        """
#        # input arguments
#        self.optMeth.lineSearchExactNewton()
#        assert 
#       
#    def testBroyden(self):
#       '''
#        Tests if goodBroyden and badBroyden gives approximately the same result
#        for a arbitrary vector x0
#        '''
#        tol=1e-5
#        x0=np.array([0,1,2])
#        H=self.optMeth.finiteDifference(g,x0)
#        if self.optProb.g(x0)<tol:
#            if super().isPosDef()==False: #Hessian is not positive definite - Error message? only stationary point found?
#                warnings.warn("Matrix at the result is not positive definite")
#            return (x,f(x))
#        sk=super().getSearchDirHessian(self.optProb.g(x0),H)
#        alfa=self.linesearch(x0,sk)
#        xk=x0+alfa*sk
#        
#        H1=self.optMeth.goodBroyden(xk,x0,self.optProb.g(xk),self.optProb.g(x0),H)
#        H2=self.optMeth.badBroyden(xk,x0,self.optProb.g(xk),self.optProb.g(x0),H)
#        self.assertAlmostEqual(H1,H2)

    def testFiniteDifference(self):
        """
        Test for the finite differnce approximation of the Hessian
        calculated for the function g (above)
        """
        xk = np.array([0,1,2])
        H = self.optMeth.finiteDifference(g(xk),xk)
        self.assertAlmostEqual(H, 2*eye(len(xk))) 
        
      



if __name__=='__main__':
    unittest.main()