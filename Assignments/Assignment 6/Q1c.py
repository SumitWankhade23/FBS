#Pascal's Triangle 
for i in range(0,4):
    
    for space in range(4 - i - 1):
        print(" ", end="")

    num = 1
    for j in range(0,i+1):
        print(num  , end =" ")
        num = num * (i-j)//(j+1)
             
    print()        