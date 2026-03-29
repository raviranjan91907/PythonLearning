#For loop is used to repeat a block of code multiple time and alos use to iterate a sequence data type like list tuple dictionary
#syntax for variable in sequence

for i in range(1,5):
    print(i)


print("------------------------------------------------------------------------------------------------")

n=[1,2,4,3,5,4,32,4]
for i in n:
    print(i,end=" ")


print("\n-------------------------------------------------------------------------------------------------")

n1=[["Raj",1],["Rohit",5],["Ayush",2],["Aarti",4]]
for i,j in n1:
    print(i," ",j)


print("------------------------------------------------------------------------------------------------")
#work the same as the above code
for i in n1:
    for j in i:
        print(j,end=" ")
    print("\n",end="")

print("\n-------------------------------------------------------------------------------------------------")


