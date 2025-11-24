
import plain_figure
from triangle_exception import *
import math

class Triangle(plain_figure.PlainFigure):
    def __init__(self, d1, d2, d3):
        if d1<=0 or d2<=0 or d3<=0:
            raise TriangleException("d1,d2,d3 must be positive")
        elif d1+d2<d3 or d1+d3<d2 or d2+d3<d1:
            raise TriangleException("Not a triangle")

        super().__init__(d1, d2, d3)
    
    def getArea(self):
        p = self.getPerimeter()/2
        return math.sqrt(p*(p-self.d1)*(p-self.d2)*
                         (p-self.d3))
    
    def getPerimeter(self):
        return self.d1+self.d2+self.d3
    
    def equals(self, pf):
        return self.getArea()==pf.getArea()
    
    def isSimilar(t1,t2):
        return t1.d1/t2.d1 == t1.d2/t2.d2 and \
            t1.d1/t2.d1 == t1.d3/t2.d3 and \
            t1.d2/t2.d2 == t1.d3/t2.d3