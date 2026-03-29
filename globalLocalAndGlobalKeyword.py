x=20 #Global variable
def local():
    x=10 #local variable
    print("inside the function and the value of x ",10)

local()
print("outside the function and the value of x ",x)

print("-------------------------------------------------------")

x1=20
def local1():
    # x1=x1+1  #this will through an error
    print("inside the function",x1)
print(x1)

print("-------------------------------------------------------")
x2=30
print("before the modifying global variable ",x2)
def local2():
    global x2
    x2+=10 # modifying the global variable with the help of using global key word
    print("inside the function ",x2)

local2()
print("outside the function ",x2)


print("-------------------------------------------------------")

def local3():
    x3=10
    print("before calling insideLocal()",x3)
    def insideLocal():
        global x3
        # x3+=10 this will through an error
        x3=50 # this will access the which is present out the all the function not the variable inside the local3()
        #this will access the global variable if not present it will create one

        print("inside the insideLocal()",x3)
    insideLocal()
    print("After calling insideLocal()",x3)

local3()
print("outside the local()",x3)
