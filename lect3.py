
import random
from collections import deque
# pip install numpy --upgrade
import numpy as np

l = []
for i in range(10):
    l.append(random.randint(-10,10))
print(l)

is_init = False
for x in l:
    if x%2 == 0:
        if not is_init:
            minx = x
            is_init = True
        elif minx > x:
            minx = x
if is_init:
    print("min=",minx)
else:
    print("No such data...")

# list comprehension
l = [random.randint(-100,100) for i in range(10)]
print(l)

ll = [x for x in l if x%2==0]
print(ll)

if len(ll) > 0:
    print("min:",min(ll))
else:
    print("No such data...")

# l1 = [int(input(f"{i}=")) for i in range(3)]
# print(l1)

# queue
# First In First Out FIFO
l.append(333)
print(l)
l.pop(0)
print(l)

# stack
# Last In First Out LIFO
l.append(444)
print(l)
print("last:",l.pop())
print(l)

# deque
dq = deque(l)
print(dq)

# FIFO
dq.append(-111)
print(dq)
dq.popleft()
print(dq)

# LIFO
dq.append(-222)
print(dq)
dq.pop()
print(dq)

# tuple immutable
t = ()
print(type(t),t)
t = (1,2,3,4,5)
print(t)
x1,x2,x3,x4,x5 = t
print(x1,x2,x3,x4,x5)
t1 = x1,x2,x3,x4
print(type(t1),t1)
t = (1,)
print(type(t),t)
t = 1
print(type(t),t)
t = (1)
print(type(t),t)

t = (1,2,3,4)
print(t[1])
# t[1] = 11

t = tuple(l)
print(type(l),l)
print(type(t),t)

print("count:",t.count(20))
if -1 in t:
    print(t.index(-1))

l11 = list(t)
print(l11)

# matrix
m = [[1,2,3],[4,5,6]]
print(type(m),m)
for row in m:
    for x in row:
        print(x, end=" ")
    print()

m = [[random.randint(0,100) for col in range(4)] 
     for row in range(3)]
print(m)

m = []
for row in range(3):
    l = []
    for col in range(4):
        l.append(random.randint(0,10))
    m.append(l)
print(m)

# m = np.matrix([[1,2],[4,5]])
# print(type(m),m)

l2 = [x for x in np.arange(0,10,2.5)]
print(type(l2),l2)