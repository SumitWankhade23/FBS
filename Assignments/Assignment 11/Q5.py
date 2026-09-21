#Python Program to Sort a List According to the Length of the Elements
#within the list.
def selectionsort(data):
    size = len(data)
    for i in range(0,size-1):
        index = i
        for j in range(i+1,size):
            if(len(data[j]) < len(data[index])):
                index = j
        data[i],data[index] = data[index],data[i]
        #print(data)


data = ["Apple","I","Egg","Pineapple","Sanjana","Go"] 
print('Before sorting: ',data)
selectionsort(data)
print('After sorting: ',data)
