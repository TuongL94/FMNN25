# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016
@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl
#import numpy as np
import unittest
from MeshWithSolve import Mesh
from MeshDyn import MeshDyn
from Node import Node
from initTestRoom import initTestRoom
from initFinalTestRoom import initFinalTestRoom
from plot import plotWholeRoom



class TestClasses(unittest.TestCase):
    """
    Test class to test the classes Mesh and Node for the third Project
    """
    
    def setUp(self):
        """
        sets up a test mesh and test nodes
        """
        self.nodeMatrix=initTestRoom() #Sets up a node matrix for a test room with stepsize 1/20
        self.finalNodeMatrix=initFinalTestRoom() #Sets up a node matrix for the expected final test room.
        self.stepsize=1/20
        self.roomNbr=2
        self.testMesh = Mesh(self.nodeMatrix,self.roomNbr,self.stepsize)
        self.finalTestMesh=Mesh(self.finalNodeMatrix,self.roomNbr,self.stepsize)
        self.nodeNeu = Node(1,2,'Neumann',10)
        self.nodeDir = Node(3,4,'Dirichlet',11)
        self.nodeInner = Node(1,2,'inner',12)
        
    def testGetNode(self):
        """
        Tests the get functions of the node class
        """
        x = self.nodeNeu.getXCoord()
        y = self.nodeDir.getYCoord()
        string = self.nodeInner.getNodeType()
        val=self.nodeNeu.getFuncVal()
        prevFuncVal=self.nodeDir.getPrevFuncVal()
        deriv=self.nodeInner.getDeriv()
        self.assertEqual([x,y,string,val,prevFuncVal,deriv],[1,4,'inner',10,11,0])
        
    def testGetMesh(self):
        '''
        Tests the get functions of the Mesh class
        '''
        nodeMatrix=self.testMesh.getNodeMatrix()
        roomNbr=self.testMesh.getRoomNbr()
        stepsize=self.testMesh.getStepsize()
        self.assertTrue(array_equal(nodeMatrix,self.nodeMatrix))
        self.assertEqual(roomNbr,self.roomNbr)
        self.assertEqual(stepsize,self.stepsize)
    
    def testSolve(self):
        '''
        Tests the resulting heat distribution for the test room
        '''
        
        self.testMesh.solveMesh()
        
        calcValMatrix=self.testMesh.getValMatrix()
        finalValMatrix=self.finalTestMesh.getValMatrix()
        #pdb.set_trace()
        plotWholeRoom(self.testMesh)
        plotWholeRoom(self.finalTestMesh) #Plotting the two temperature distributions in order to compare visually
        self.assertTrue(np.allclose(calcValMatrix,finalValMatrix,rtol=0,atol=0.0001)) #Tolerence of 0.0001 degreee absolute difference
        
    def testSolveMatrices(self):
        '''
        Compares the different solve matrices (dynamic and static)
        '''
        lapA, rhs = MeshDyn.setupSolveMatrixAndRhs()
        solVec = MeshDyn.solveMesh(lapA,rhs)
        solMat = np.reshape(solVec,MeshDyn.numberOfYnodes,MeshDyn.numberOfXNodes)
        finalValMatrix=self.finalTestMesh.getValMatrix()
        np.testing.assert_allclose(solMat, finalValMatrix,rtol=0,atol=1e-5)
        #self.testMesh.plotRoomPart()
        #self.finalTestMesh.plotRoomPart() #Plotting the two temperature distributions in order to compare visually
        #self.assertTrue(allclose(calcValMatrix,finalValMatrix,atol=1)) #Tolerence of 1 degreee absolute difference       
        

if __name__=='__main__':
    unittest.main()        

