def linerSearch(data,ele):
    for i in range(0,len(data)):
        if(ele == data[i]):
            return i
    else:
        return -1


data = [10,25,26,45,7,5,45,75,85,79,99,45,76] 
ele = int(input("Enter element: "))
result = linerSearch(data,ele)
if(result != -1):
    print(f"{ele} is presnt at index {result}")
else:
    print(f"{ele} is not presnt")       