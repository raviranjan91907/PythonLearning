#Dictionary is nothing but key value pairs

#initilizeing the dictionary
d1={} #empty dictionary
print(type(d1))


d2={
    "Aarti":"Burger",
    "Rohan":"Fish",
    "Neha":"Roti"
}
print(d2)
print(d2["Aarti"])
print(d2["Rohan"])

#Dictionary inside dictionary
d3={
    "Aarti": "Burger",
    "Rohan": "Fish",
    "Neha": "Roti",
    "Shubham":{"B":"Maggie","L":"Roti","D":"Chicken"}
}
print(d3["Shubham"])
print(d3["Shubham"]["B"])
print(d3["Shubham"]["L"])

d3["Rohit"]="Junk Food" #entering new data inside the existing dictionary
print(d3["Rohit"])

# del d3["Rohit"] #deleting the data from the dictionary
# print(d3["Rohit"]) #this will give an error

print(d3)
d4=d3 #this will not create a new dictionary this will create a d4 pointer which point to d3 if we made change in d4 then d3 will also get change
del d4["Rohit"]
print(d3)

d5=d3.copy()
del d5["Rohan"]
print(d3)

print(d3.get("Aarti"))

d3.update({"Robin":"Burger"})
print(d3)


print(d3.keys()) #This will print all the key in the dictionary
print(d3.items())

#Create a dictionary and take input form the user and return the meaning of the word from the dictionary
