for i in range(1,6):
    for j in range(1,i+1):
        if(j == 5):
            continue
        print(j,end=" ")
    
    for j in range(5-i,0,-1):
        print(" ",end=" ")

    for j in range(1,5-i):
        print(' ', end = " ")
   
    for j in range(i,0,-1):
        print(j,end = " ")
        
    print() 
