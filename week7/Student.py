
from StudentError import StudentError

class Student:
    def __init__(self,fNum=0,name="",avMark=0):
       self.fNum = fNum
       self.name = name
       self.avMark = avMark

    def __str__(self):
        return f"({self.fNum},{self.name},{self.avMark})"

    def __repr__(self):
        return f"({self.fNum},{self.name},{self.avMark})"

    def getFNum(self):
        return self.fNum
    
    def setFNum(self,fNum):
        if fNum <= 0:
            raise StudentError("Not a valid Faculty Number")
        self.fNum = fNum

    def getName(self):
        return self.name
    
    def setName(self,name):
        if name == "" or len(name) < 2:
            raise StudentError("Not valid name")
        self.name = name
    
    def getAvMark(self):
        return self.avMark
    
    def setAvMark(self,avMark):
        if avMark < 2 or avMark > 6:
            raise StudentError("Not a valid avMark")
        self.avMark = avMark