
class PlainFigure:
    def __init__(self,d1,d2,d3):
       self.d1 = min(d1,min(d2,d3)) 
       self.d3 = max(d1,max(d2,d3))
       self.d2 = d1+d2+d3-(self.d1+self.d3)
    
    def __str__(self):
        return f"({self.d1},{self.d2},{self.d3})"
    
    def __repr__(self):
        return f"({self.d1},{self.d2},{self.d3})"
    
    def equals(self, pf):
        return self.d1 == pf.d1 and  \
            self.d2 == pf.d2 and  \
            self.d3 == pf.d3
    
    def getArea(self):
        pass

    def getPerimeter(self):
        raise NotImplementedError()
    
    def print(self):
        print(self)