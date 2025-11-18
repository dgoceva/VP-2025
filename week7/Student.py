
class Student:
    def __init__(self,fNum=0,name="",avMark=0):
       self.fNum = fNum
       self.name = name
       self.avMark = avMark

    def __str__(self):
        return f"({self.fNum},{self.name},{self.avMark})"

    def __repr__(self):
        return f"({self.fNum},{self.name},{self.avMark})"  