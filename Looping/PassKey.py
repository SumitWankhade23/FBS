#1 Pass is keyword use to neglect expected indented block error 
for i in range(1,10):
    pass

#2. Break- to terminate the loop 
for i in range(1,10):
    if(i == 3):
        break
    print(i)

#3. contine- to stop current iteration
for i in range(1,10):
    if(i == 3):
        continue
    print(i)

#4. else: This will execute after complition of loop execution 
for i in range(1,10):
    if (i == 3):
        break
    print(i) 
else:
    print("Loop has succesfullly executed")        
       