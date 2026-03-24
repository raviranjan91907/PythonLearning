#initializing a set
s1=set() #this is an empty set

l=[1,2,3,4,3,3,3,4]
s2=set(l) #remove duplicate
print(l)
print(s2)

s2.add(1) #add only unique element
s2.add(5)
s2.add(6)
print(s2)

print(s2.union({1,2,3,11}))
print(s2.intersection({1,2,3,11}))
print(s2.difference({1,2,3,11}))

print(s2.isdisjoint({1,2,3,11}))
print(s2.isdisjoint({12,34,45}))

s2.remove(1)
print(s2)

