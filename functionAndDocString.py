#function->it is a block of code which can do a specific task and can be reuse
#function type-> builtin function and user define function

#builtin function->which is already there in python
n=[1,2,3,4,5]
print(sum(n))
print(max(n))
print(min(n))



#user define function->the function which user define or create in python
#                       by using "def" keyword

#without argument
def function1():
    print("Hello this is user define function")
function1()


#with argument
def function2(a, b):
    print("this is user define function2 and value of a+b",a+b)
function2(1,5)


#with argument and return value
def function3(a,b):
    c=(a+b)/2
    return c
x=function3(1,5)
print(x)


#DocString->this is a special string which use to describe what function ,class or module do and its writen inside the triple quotes (''' or """ )
def function4(a,b):
    """This function is use to calculate the sum of two numbers"""
    return (a+b)/2
print(function4.__doc__)
print(function4(3,565))