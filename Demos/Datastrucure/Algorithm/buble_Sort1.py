def buble_sort(data):
    n = len(data)    
    for i in range(1,n):
        for j in range(0,n-i):
            if(data[j] > data[j +1]):
                data[j],data[j+1]=data[j+1],data[j] 
                print(data)            

data = [60,50,40,30,20,10]
print('Before sorting',data)
buble_sort(data)
print('after sort',data)

    