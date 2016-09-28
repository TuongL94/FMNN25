import unittest
from OptimizationProblem import OptimizationProblem
from QuasiNewton import QuasiNewton, MethodType
from OptimizationMethods import OptimizationMethods
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
def rosf(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
def rosg(x):
    return 2*np.array([200*(x[1]-x[0]**2)*(-x[0])-(1-x[0]),100*(x[1]-x[0]**2)])    

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
        self.optProbRos=OptimizationProblem(rosf,rosg)
        self.optMethRos=QuasiNewton(self.optProbRos,MethodType.CLASSICALNEWTON)

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
        
#    def testLineSearchExact(self):
#        """
#        Test for the linesearch methods
#        Compares the steepest descent solution to the one found by Newton's method        
#        """
#        xk = 2
#        sk = -4
#        alphaSteep = self.optMeth.lineSearchExactSteepestDesent(xk,sk)
#        alphaNewt = self.optMeth.lineSearchExactNewton(xk,sk)
#        self.assertAlmostEqual(alphaSteep,alphaNewt,places=5) 
        
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
        xr = np.array([1,1])
        H1 = self.optMeth.finiteDifference(xk)
        H2 = self.optMethRos.finiteDifference(xr)
        print(H2)
        print(H1)
        np.testing.assert_allclose(H1, 2*eye(len(xk)),0,1e-5)
        np.testing.assert_allclose(H2,2*np.array([[400*xr[0]-200*(xr[1]-xr[0]**2)+1,-200*xr[0]],[-200*xr[0],100]]),0,1e-5)
        
    def testbfgs(self):
        """
        Tests if the bfgs update works for arbitrary inputs. The method should give an identity matrix.
        """
        xkPlusOne = transpose(2*np.array([1.0,1.0,1.0]))
        xk = transpose(np.array([1.0,1.0,1.0]))
        gkPlusOne = xkPlusOne
        gk = xk
        H0 =  np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
        updatedH = OptimizationMethods.bfgs(self,xkPlusOne,xk,gkPlusOne,gk,H0)
        realResult = H0
        np.testing.assert_array_almost_equal(updatedH,realResult,8,"The bfgs update is not returning the expected result.")

    def testdfp(self):
        """
        Tests if the bfd update works for a specific input.  The method should give an identity matrix.
        """
        xkPlusOne = transpose(2*np.array([1.0,1.0,1.0]))
        xk = transpose(np.array([1.0,1.0,1.0]))
        gkPlusOne = xkPlusOne
        gk = xk
        H0 =  np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
        updatedH = OptimizationMethods.dfp(self,xkPlusOne,xk,gkPlusOne,gk,H0)
        realResult = H0
        np.testing.assert_array_almost_equal(updatedH,realResult,8,"The dfp update is not returning the expected result.")


if __name__=='__main__':
    unittest.main()
