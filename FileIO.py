#File Io Basics
"""
"r"-> Open file for reading default mode
"w"-> Open file for writing
"x"->create file if not exists
"a"->Add more content to a file (append mode)
"t"->open filein text mode
"b"-> open file in binary mode
"+"->Read and write mode
"""

f=open("sample.txt")
#here open("sample.txt") returns file pointer
#this file is open in read mode which is default mode
content=f.read()
print(content)
f.close()

print("-------------------------------------------------------")

f=open("sample.txt","rt") #opening in read text mode
content1=f.read(3) #read 3 character of the file
content2=f.read(3)
print(content1)
print(content2)
f.close()

print("-------------------------------------------------------")


f=open("sample.txt","rb") #opening in read binary mode
content=f.read()
print(content)
f.close()

print("-------------------------------------------------------")

#reading the file line by line
f=open("sample.txt","rt")
for line in f:
    print(line,end="")


print("\n","-------------------------------------------------------")
f=open("sample.txt","rt")
print(f.readline(),end="") #this will read the first line of the file
print(f.readline()) #after reading the point will move to the next line so it wil read second line
f.close()

print("-------------------------------------------------------")
f=open("sample.txt","rt")
print(f.readlines()) #this function will read the content of the file and store it in a list
f.close()