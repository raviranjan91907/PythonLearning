#A list is a collection of items of different or same datatypes
n=[]
n1=[1,2,3,4,"hello",True,False,1.3]


n2=[132,2,1,22,2,33,23,112,212,442,2334,23]
n2.sort() #this will sort the list in ascending order
print(n2)
n2.sort(reverse=True) #this will sort the list in descending order
print(n2)


print(len(n2))
print(max(n2))
print(min(n2))

n.insert(0,"hello")
n.insert(1,"world")
print(n)
print(n.index("hello"))


n.append("Indian")
print(n)

n.remove("hello")
print(n)


n.pop(0)
print(n)
n.pop()
print(n)