
from Student import Student
from Group import Group
from StudentError import StudentError

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
    print(group.group[0].getFNum())
    print(group.group[0].getName())
    print(group.group[0].getAvMark())
    try:
        group.group[0].setFNum(int(input("FNum=")))
        group.group[0].setName("")
        group.group[0].setAvMark(1)
        group.group[0].setFNum(0)
        print(group)
    except ValueError as e:
        print(e)
    except StudentError as e:
        print(e)
    print(group)
