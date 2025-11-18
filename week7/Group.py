
class Group:
    def __init__(self, group=None):
        if group==None:
           group = []
        self.group = group 

    def __str__(self):
        return str(self.group)
    
    def __repr__(self):
        return str(self.group)
    
    def addStudent(self,student):
        if student not in self.group:
            self.group.append(student)
    
    def delStudent(self,student):
        if student in self.group:
            self.group.remove(student)
    
    def delStudentByFNum(self,fNum):
        for i in range(0,len(self.group)):
            student = self.group[i]
            if student.fNum == fNum:
                self.group.remove(student)
                return
    
    def delStudentByAvMark(self,avMark):
        stList = []
        for student in reversed(self.group):
            if student.avMark<=avMark:
                stList.append(student)
                self.group.remove(student)
        return stList