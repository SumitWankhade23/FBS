#3. Write a program to find the second largest element in the list.
def secondLarg_el(data):
    size = len(data)
    smax = 0
    max = data[0]
    for i in range(1,size):
        if(max < data[i]):
            smax = max
            max = data[i]
        elif(smax < data[i]):
            smax = data[i]    
    return smax,max

data = [10,20,52,2,45,75,22,40,35,50] 
res = secondLarg_el(data) 
print(f"Second largest element = {res[0]}")
print(f"Largest element = {res[1]}")      
