import unittest
from CSpline import CSpline
from scipy import *

class TestCSpline(unittest.TestCase):

    def setUp(self):
        controlPoints = array([[1,2],[3,4],[3,5],[3,6],[4,6]])
        nodes = array([0,1,2,3,4,5,6])
        self.cSpline=CSpline(controlPoints,nodes)

    def testDeBoorVsBasis(self):
        u = 2.5
        iPlusOne = (self.cSpline._nodes > u). argmax ()
        firstBasisFunction = self.cSpline.getBasisFunction(iPlusOne-3)
        secondBasisFunction = self.cSpline.getBasisFunction(iPlusOne-2)
        thirdBasisFunction = self.cSpline.getBasisFunction(iPlusOne-1)
        fourthBasisFunction = self.cSpline.getBasisFunction(iPlusOne)
        leftSide = self.cSpline(u)
        rightSide = self.cSpline._controlPoints[iPlusOne-3]*firstBasisFunction(u) + \
        self.cSpline._controlPoints[iPlusOne-2]* secondBasisFunction(u) + self.cSpline._controlPoints[iPlusOne-1]*\
        thirdBasisFunction(u) + self.cSpline._controlPoints[iPlusOne]* fourthBasisFunction(u)
        self.assertTrue(array_equal(leftSide,rightSide)," The left-hand side and right-hand side are not equal.")

    #Testing the call function s(u) in the class CSpline
    #The call function s(u) should not work for u:s that are outside of the defined
    #interval nodes(2)<=u<=nodes(K-2)
    def testCallFunction(self):
        #Finding the minimum and maximum allowed node values
        self.assertRaises(Exception,self.cSpline.__call__,0)

    #Testing that the basis functions adds up to unity at point u
    def testUnityOfBasisFunction(self):
        u = 2.5
        length=len(self.cSpline._controlPoints)
        sum=0
        for j in range(length):
            sum += self.cSpline.getBasisFunction(j)(u) #Need the name and specs of the "Task3" function
        self.assertAlmostEqual(1.0,sum,msg='Basis function does not sum up to unity')

    #Testing that the de Boor algorithm gives the same result as the defined function
    def testEquality(self):
        u = 2.5
        length=len(self.cSpline._controlPoints)
        sum = array([0.0,0.0])
        for j in range(length):
            sum += self.cSpline.getBasisFunction(j)(u)*self.cSpline._controlPoints[j]
        self.assertTrue(allclose(self.cSpline(u),sum),msg='Algorithm not equal to basis functions result')













