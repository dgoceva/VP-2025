
from triangle import Triangle
from triangle_exception import TriangleException

if __name__ == "__main__":
    t1 = Triangle(3,4,5)
    t2 = Triangle(4,3,5)
    t3 = Triangle(2,3,4)
    t1.print()
    print(t2)
    t3.print()
    print(t1.equals(t2))
    print(t1.equals(t3))
    print(Triangle.isSimilar(t1,t2))
    print(Triangle.isSimilar(t2,t3))
