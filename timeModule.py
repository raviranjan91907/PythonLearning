import time
k=0
initialTime=time.time()
while k<45:
    time.sleep(2) #this make sleep the loop for 2 second for every iteration
    print(k)
    k+=1

print("while loop running time: ",time.time()-initialTime)

initialTime2=time.time()
for i in range(45):
    print(i)

print("for loop running time: ",time.time()-initialTime2 )

localTime=time.asctime(time.localtime(time.time()))
print(localTime)
