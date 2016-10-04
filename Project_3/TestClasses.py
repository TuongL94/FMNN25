# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:39:00 2016

@author: Anders Hansson, Tuong Lam, Bernhard Pöchtrager, Annika Stegie
"""
import scipy as sp
import pylab as pl
import unittest
from Mesh import Mesh
from Node import Node


class TestClasses(unittest.TestCase):
    """
    Test class to test the classes Mesh and Node for the third Project
    """
    
    def setUp(self):
        """
        sets up a test mesh and test nodes
        """
        self.mesh1 = Mesh(1,2,0.1)
        self.nodeNeu = Node(1,2,'Neumann')
        self.nodeDir = Node(3,4,'Dirichlet')
        self.nodeNorm = Node(1,2,'normal')
        
    def testGetNode(self):
        """
        tests the get functions of the node class
        """
        x = self.nodeNeu.xCoord
        y = self.nodeDir.yCoord
        string = self.nodeNorm.nodeType
        self.assertEqual([x,y,string],[1,4,'normal'])

 def testGetMesh(self):
        """
        tests the get functions of the mesh class
        """
               
        
        

if __name__=='__main__':
    unittest.main()        

