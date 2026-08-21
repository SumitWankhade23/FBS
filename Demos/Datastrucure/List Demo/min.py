data = [10,20,30,9,45,78,45,98,40,50,60]

min = data[0]
for i in range(0,len(data)):
    if(min > data[i]):
        min = data[i]
print(min)        