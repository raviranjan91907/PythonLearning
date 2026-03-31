def function_name_print(a,b,c,d):
    print(a,b,c,d)
function_name_print("Harry","Rohan","Skillf","Hammd")
"""
now if we put one more argument in the function function_name_print it will give an error
so for that we have to add one more Parameter in the function_name_print but it is not good
for the scalable program
"""

print("----------------------------------------------------------------------")
"""
*args lets you pass any number of positional arguments (as a tuple).
Rule of putting *args in parameter that NormalArgs should come first
"""

def functionAgrs(NormalArgs,*args):
    print(type(args))
    print(NormalArgs)
    for i in args:
        print(i)

har=["harry","Rohan","skillf","Hammd","hello",1]
functionAgrs(1,*har)
normal="this is normal Argument"
functionAgrs(normal) #it ok to not put *args in argument

print("----------------------------------------------------------------------")

"""
**kwargs lets you pass any number of keyword arguments (as a dictionary).
Rule of putting *args in parameter that NormalArgs should come first then *args if they are there in the parameter
"""

def functionAgrs2(NormalArgs,*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    for i ,j in kwargs.items():
        print(f"{i} is {j}")


print("------------------------------------------------------------------------")

kw={"Rohan":"Monitor","Harrv":"Fitness Instructor","Aarti":"Programmer",
    "shivam":"cook"}
functionAgrs2(normal,*har,**kw)


print("--------------------------------------------------------------------------------")
def fun(dic):
    for i,j in dic.items():
        print(f"{i} is {j}")

fun(kw)