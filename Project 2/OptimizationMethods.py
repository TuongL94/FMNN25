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

        :return:
        """
        h = # preallocate matrix of size len(xk)*len(xk)? Or just append?
        for i in range(len(xk)):
            for j in range(len(xk)):
                h[i,j] = (optProb.g(xk[i]+0.5e-5)[j]-optProb.g(xk[i]-0.5e-5)[j])/1e-5
        h = 1/2*(h+h.T)


