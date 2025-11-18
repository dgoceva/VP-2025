
from Student import Student
from Group import Group

if __name__=="__main__":
    group = Group()
    group.addStudent(Student(111,"Ivan Ivanov",5.65))
    group.addStudent(Student(222,"Petyr Petrov",5.66))
    group.addStudent(Student(333,"Ivan Petrov",4.66))
    group.addStudent(Student(444,"Petyr Ivanov",3.66))
    group.addStudent(Student(555,"Georgi Georgiev",5.66))
    print(group)
    group.delStudentByFNum(505)
    group.delStudentByFNum(222)
    print(group)
    print(group.delStudentByAvMark(5))
    print(group)
