import random

print("Hello Pyhon!")
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2//3)
print(2%3)
print(2**3)
print()

for x in range(1,100):
    print(x)

print()
for x in range(1,101):
    print(x)

print()
for x in range(1,101,2):
    print(x)

# sum = 0

# # sum = 0+3 = sum+3 = 3
# # sum = 3+5 = sum+5 = 8

# for i in range(3):
#     x = int(input(f"[{i+1}]="))
#     sum += x
# print("sum = ",sum)

# numbers = int(input("How many numbers you want to sum? "))
# sum = 0
# for i in range(numbers):
#     x = int(input(f"[{i+1}]="))
#     sum += x
# print("sum = ",sum)

# numbers = int(input("How many numbers you want to sum? "))
# sum = 0
# for i in range(numbers):
#     x = int(input(f"[{i+1}]="))
#     sum += x
# print("sum = ",sum)

numbers = int(input("How many numbers you want to sum? "))
sum = 0
for i in range(numbers):
    x = random.randrange(-10,10)
    print(x,end = " ")
    sum += x            # sum = sum + x
print("\nsum = ",sum,"average = ",sum/numbers)

numbers = int(input("How many numbers you want to multiply? "))
mult = 1
for i in range(numbers):
    x = random.randrange(-10,10)
    print(x,end = " ")
    mult *= x            # mult = mult * x
print("\nmult = ",mult)

sum = 0
min = 0
while True:
    x = int(input("x= "))
    if x == 0:
        break
    sum += x
    if min == 0:
        min = x
    elif min > x:
        min = x
print("sum=",sum,"min = ",min)

sum = 0
is_init = False
while True:
    x = int(input("x= "))
    if x == 0:
        break
    sum += x
    if not is_init:
        min = x
        is_init = True
    elif min > x:
        min = x
print("sum=",sum,"min = ",min)

is_init = False
while True:
    x = int(input("x= "))
    if x == 0:
        break
    if x % 2 == 0:
        if not is_init:
            max_even = x
            is_init = True
        elif max_even < x:
            max_even = x
if is_init:
    print("max even = ",max_even)
else:
    print("No such data...")