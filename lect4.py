
# set
s= set()
print(type(s),s)
s = {1,2,3,4,5,1}
print(s, len(s))
s = {"abracadabra"}
print(s)
s = set("abracadabra")
print(s)

s = {x for x in range(10) if x%2==0}
print(s)

s1 = {1,2,3,4,5}
s2 = {1,2,6,7}
print(s1.difference(s2), s1-s2)
print(s1.union(s2), s1|s2)
print(s1.intersection(s2), s1&s2)
print(s1.symmetric_difference(s2),s1^s2)
s.clear()
print(s)
del s
# print(s)
s1.difference_update(s2)
print(s1,s2)
s1 = {5,4,1,2,3}
s1.symmetric_difference_update(s2)
print(s1,s2)
s1 = {5,4,1,2,3}
s1.intersection_update(s2)
print(s1,s2)
s1.update([1,11,32,3,4,"abc"])
print(s1)
s1.add(44)
print(s1)
# s1.add([1,11,22])
s1.add(1)
print(s1)
print(s1.issubset(s2),s1.issuperset(s2))
print(s1<=s2,s1>=s2)

fs = frozenset([1,2,"abd"])
print(fs)

# year = input("Input year: ")
# print(type(year),year)
# syear = set(year)
# print(type(syear),syear)
# print(len(syear)==len(year))

# dict
d = {}
print(type(d),d)
d = {1:"one",2:"twoo"}
print(d)
print(d[2])
d[3] = "three"
print(d)
d[2] = "two"
print(d)
print(d.get(4))
print(d.get(4,11))
print(d.items())
print(d.keys())
print(d.values())

for k,v in d.items():
    print(k,"->",v)
for k in d.keys():
    print(k)
for i,v in enumerate(d.values()):
    print(i,v)
for i,d in enumerate(d.items()):
    print(i,d)
# for i,el in enumerate(d[0]):
#     print(i,el)

d = dict([(1,"one"),(2,"two")])
print(d)
s = {(x,x**3) for x in range(10)}
print(type(s),s)
d = {x:x**3 for x in range(10)}
print(type(d),d)

d1 = d.fromkeys(d.keys())
print(type(d1),d1)

d.update([(11,"eleven")])
print(d)

for k,v in reversed(d.items()):
    print(k,v)

# for el in reversed(s1):
#     print(el)
for el in s1:
    print(el)

d.clear()
print(d)
del d
# print(d)
d = {x:x*2 for x in range(5)}
print(type(d),d)
d1 = d.copy()
print(type(d1),d1)
print(3 in d1)
print(3 in d1)
print(11 in d1)

print(d1.popitem())
print(d1)
print(d1.pop(0))
print(d1)
if 11 in d1:
    print(d1.pop(11))

print(sorted(d1,reverse=True))
l = [x**2 for x in range(5)]
print(l)
l.sort(reverse=True)
print(l)
print(sorted(l, reverse=True))
print(sorted(s))