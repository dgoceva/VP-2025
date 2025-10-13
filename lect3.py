
import random

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

l1 = [int(input(f"{i}=")) for i in range(3)]
print(l1)

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