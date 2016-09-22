# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:23:09 2016
@authors: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
from  scipy import *
from  pylab import *

class OptimizationMethods:

    def lineSearchExact(self):
        """
        
        :return:
        """
        # several methods possible
        # for example again a Newton Method, Bisection, Steepest descent
        
        # Bisection
        # actually not such a nice method because the sign-change has to be detected
        # evalute f at different points around xk to detect sign change
        leftEnd = #nearest point to the left of sign change
        rightEnd = #nearest point to the right of sign change
        # a starting alpha is needed, maybe take 1?
        # have to find min of fAlfa, root of gAlfa
        gAlfa = g(alfa*xk)
        alfa = (rightEnd-leftEnd)/2       
        while gAlfa > tol:
            if gAlfa == 0:
                return alfa
            elif gAlfa*f(leftEnd*xk) < 0:
                rightEnd = alfa
            else :
                leftEnd = alfa
            alfa = (rightEnd-leftEnd)/2
            gAlfa = g(alfa*xk)
            # it shoukd be checked if this is really a min or any other stationary point
            if (g((alfa+0.5e-5)*xk)-g((alfa-0.5e-5)*xk))/1e-5 <= 0:
                #what should be done here?
        return alfa
        
        # Newton Method
        # a starting alpha is needed, maybe take 1?
        CN = QuasiNewton(#fAlfa function and gradient must be put in; no line search, finite difference approx of H)
        alfa = CN.solve(alfa)
        
        # Steepest descent method
        # starting alfa
        beta = 1/2   #parameter tuning possible
        gamma = 1e-2 #parameter tuning possible
        while g(alfa*xk) > tol:
            # stepsize calculated by Armijo's method              
            exponent = 1
            stepsize = 1
            while f(alfa-stepsize*g(alfa*xk))-f(alfa*xk) <= -stepsize*gamma*norm(g(alpha*xk))**2:
                stepsize = beta**exponent
                exponent = exponent+1
            alfa=alfa-stepsize*g(alfa*xk)
        # check if really min or just stationary point  
        if (g((alfa+0.5e-5)*xk)-g((alfa-0.5e-5)*xk))/1e-5 <= 0:
                #what should be done here?    
        return alpha
            
                
                
                
                
            

    def lineSearchInexact(self):
        """

        :return:
        """

    def dfp(self):
        """

        :return:
        """

    def bfgs(self):
        """

        :return:
        """

    def broydenGood(self):
        """

        :return:
        """

    def broydenBad(self):
        """

        :return:
        """

    def lineSearch(self):
        """ Global linesearch method, inherit this method in QuasiNewton.py. This method acts as a placeholder,
        DONT IMPLEMENT ANYTHING HERE!

        """

    def findHessian(self):
        """ Global method for finding the hessian, inherit this method in QuasiNewton.py. This method acts as a placeholder,
        DONT IMPLEMENT ANYTHING HERE!
        """

    def updateHessian(self):
        """

        :return:
        """
    def finiteDifference(self):
        """
        Does a simple central finite difference approximation of the hessian at point xk
        :return: h, symmetrized finite difference approximation of Hessian
        """
        h = # preallocate matrix of size len(xk)*len(xk)? Or just append?
        for i in range(len(xk)):
            for j in range(len(xk)):
                h[i,j] = (optProb.g(xk[i]+0.5e-5)[j]-optProb.g(xk[i]-0.5e-5)[j])/1e-5
        h = 1/2*(h+h.T)
        return h


