# if elif else is a conditional statement block in while if a condition is for the block then the block will execute

num=int(input("Enter a number: \n"))
if num%2==0:
    print("The input number is Even")
else:
    print("The input number is odd")


age=int(input("Enter your age:\n"))
if age<18:
    print("You are not eligible for vote")
elif age==18:
    print("you are 18 year old try next year")
else:
    print("you are eligible for vote")



#write a program that give user 3 chance to guess the number if it guesses the right number within the 3 chances the print winner else try next time
i=0
actualNumber=43
b=True
while i<3:
    num = int(input("Guess a number: \n"))
    if num>actualNumber:
        print("Your number is greater than the actual number")
    elif num<actualNumber:
        print("Your number is less than the actual number")
    else:
        print("You guessed the right number")
        b=False
    i+=1

if b:
    print("Try next Time")



