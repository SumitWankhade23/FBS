#2. Write a program to find maximum and minimum element in a list.
def max_of_List(data):
    size = len(data)
    el_min = data[0]
    el_max = data[0]
    for i in range(1,size):
        if(el_max < data[i]):
            el_max = data[i]
            #print(max) 
        elif(el_min > data[i]):
            el_min = data[i] 
    return el_max, el_min

data = [10,12,2,15,20,60,25,30,35,40]
result = max_of_List(data)
print(f"Maximum and minimum element of list {result}")
