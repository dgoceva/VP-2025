
# 1,1
# n = (n-1) + (n-2)
n1 = n2 = 1
print(n1,n2,end=" ")
for i in range(10-2):
    n1,n2 = n1+n2,n1 
    print(n1,end=" ")
print()