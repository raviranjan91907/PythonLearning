#String Slicing is the way of extracting the part (substring) from a string
#Syntax-> String[start:stop:step]
#Start->starting index (inclusive)
#Stop->ending index (exclusive)
#step->no. of character to skip

str="This is my python learning"
print(str[0:5])
print(str[:5])
print(str[1])
print(str[2:])
print(str[::-1]) #this will reverse the string
print(str[::-3],) #this will frist reverse the string and then skip 3 character

# STRING FUNCTIONS

#string.isalnum()
#-> return true if all character are letter or number
#-> Return false if there is any space,symbol,empty string

print(str.isalnum(),end=" ")
print("123".isalnum(),end=" ")
print("hell123".isalnum(),end=" ")
print("hello 123".isalnum(),end=" ")
print("hello@".isalnum(),end=" ")
print("".isalnum())

#string.isalpha()
#->return is all the character is letter
#->return false if string contains->number,space,special character or empty string
print(str.isalpha(),end=" ")
print("123".isalpha(),end=" ")
print("hell123".isalpha(),end=" ")
print("hello 123".isalpha(),end=" ")
print("hello@".isalpha(),end=" ")
print("".isalpha())

#string.endswith(suffix,start,end) suffix->ending you u want to check,start->starting index,end->ending index
#return is string end with suffix otherwise return false
print("Hello World".endswith("World"))
print("Hello World".endswith("Hello"))
print("file.txt".endswith((".txt", ".pdf")))
print("Hello World".endswith("lo", 0, 5))


#string.count(substring, start, end) substring → the text you want to count (required),start → starting index (optional),end → ending index (optional)
#return number of occurrence of the string passed if not found return 0
print("hello world".count("o"))
print("apple apple banana".count("apple"))
print("hello".count("z"))
print("hello hello".count("lo", 0, 5))
print("Hello".count("h") )
print("aaa".count("aa") )# 1 (not 2)
print("apple applebanana".count("apple")) #(return 2 not 1)


