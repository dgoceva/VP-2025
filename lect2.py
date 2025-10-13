
import random

l = [1,2,3,4,5]
print(l)

# l = []
# for i in range(5):
#     x = int(input(f"{i+1}:"))
#     l.append(x)

# print(l)

l = []
for i in range(5):
    l.append(random.randint(-10,10))

print(l)

sum = 0
for i in range(len(l)):
    sum += l[i]

print("sum=",sum)

sum = 0
for x in l:
    sum += x

print("sum = ",sum)

print("min=",min(l))
print("max= ",max(l))

# ll = input().split(",")
# print(ll)
# ll.append([1,2,3])
# print(ll)

ll = [[1,2,3],
      [11,12,13],
      [-1,-2,-3]]
print(ll)

for x in ll:
    print(x)

for x in ll:
    for y in x:
        print(y,end=" ")
    print()

print(l)
print(l[1])
print(l[-1])
# print(l[10])  IndexError: list index out of range
print(l[-5])


print(l)

# slices
print(l[1:3])
print(l[1:])
print(l[:4])
print(l[-2:])
print(l[:-3])
print(l[-2:-4])
print(l[-4:-2])
print(l[:])

print(l)
l[1] = [11,12,13]
print(l)
l += [-1,-2,-3]  # l = l + [-1,-2,-3]
print(l)
del l[0]
print(l)
del l[2:4]
print(l)
del l[:]
l.clear()
print(l)
del l
# print (l)  NameError: name 'l' is not defined.

l = []
for i in range(5):
    l.append(random.randint(-10,10))
l += [1,1]
print(l)

print(l.count(1))
print(l.index(1))
print(l.index(1,l.index(1)+1))
l.insert(0,[1,1])
print(l)
l[0] += [2,2]
print(l)
# l[3] += [2,2]  TypeError: unsupported operand type(s) for += int and list

# l[0] += 14
l[0] += [14]
print(l)

l.remove(1)
print(l)
# l.remove(11)  ValueError
if 1 in l:
    l.remove(1)

print(8>>1)
print(-8>>2)
print(2<<4)