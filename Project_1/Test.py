from CSpline import CSpline
import SplineDemo as SplineDemo
from numpy import *

nodes=array([0,0,1,3,4,4,4])
s=CSpline(array([[1,2],[3,4],[1,5],[3,6],[4,6]]),nodes)
a = CSpline.makeDeBoorPoints(array([1,1,1,4,5,9,9,9]),array([[1], [2],[3],[4],[5],[6] ]), array([[5],[6],[7],[8],[9],[11]]))
print(a)
s.plot() # plot function does not work when the content of this file is moved from CSpline.py!


(controlPoints1,nodes1)=SplineDemo.spline()
s1=CSpline(array(controlPoints1),array(nodes1))
s1.plot()
(controlPoints2,nodes2)=SplineDemo.spline(False)
s2=CSpline(array(controlPoints2),array(nodes2))
s2.plot()