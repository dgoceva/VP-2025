
# 1,1
# n = (n-1) + (n-2)

def fib():
    n1 = n2 = 1
    print(n1,n2,end=" ")
    for i in range(10-2):
        n1,n2 = n1+n2,n1 
        print(n1,end=" ") 
    print()

def fib1(count):
    n1 = n2 = 1
    for i in range(count):
        print(n2,end=" ") 
        n1,n2 = n1+n2,n1 
    print()
def fib2(limit):
    n1 = n2 = 1
    while(n2<=limit):
        print(n2,end=" ") 
        n1,n2 = n1+n2,n1 
    print()
def fib11(count):
    n1 = n2 = 1
    fibList = []
    for i in range(count):
        fibList.append(n2) 
        n1,n2 = n1+n2,n1 
    return fibList
def fib22(limit):
    n1 = n2 = 1
    fibList = []
    while(n2<=limit):
        fibList.append(n2) 
        n1,n2 = n1+n2,n1 
    return fibList
def fib222(limit=1000):
    n1 = n2 = 1
    fibList = []
    while(n2<=limit):
        fibList.append(n2) 
        n1,n2 = n1+n2,n1 
    return fibList
fib()
fib1(20)
fib1(25)
print(type(fib),fib,fib())
fib2(100)
fib2(13)
print(fib11(10))
print(fib22(100))
# print(fib22())
print(fib222())
print(fib222(10))