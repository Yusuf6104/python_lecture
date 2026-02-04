#loop in python
count = 1 
while count <= 5 : # while loop
    print("hello")
    count+=1

print(count)    

i = 1 
while i <= 100:
    print("helloworld",i)
    i+=1

# print numbers from 1 to 5
i=1 #iteration
while i<=5: #always write condition
    print(i)
    i += 1 #iterator
    
print("Loop ended")       

#  continue 
i = 1
while i <= 10:
    if(i%2 == 0):#for odd no
        i += 1
        continue #skip
    print(i)
    i += 1
#  break 
i = 1
while i <= 10:
    if(i%2 != 0): #for evem no
        i += 1
        break
    print(i)
    i += 1

           
           