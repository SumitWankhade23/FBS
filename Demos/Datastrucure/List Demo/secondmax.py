#Check second max element from list
data = [10,20,30,99,45,78,98,40,50,60]

max = data[0]
s_max = []
for ind in range(1, len(data)):
    if max < data[ind]:
        s_max = max
        max = data[ind]
    elif(s_max < data[ind]):
        s_max = data[ind]

print("second Maximum: ",s_max)    


    