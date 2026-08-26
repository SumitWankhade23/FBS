def selectionsort(li):
    size = len(li)
    for i in range(0,size-1):
        min_ind = i
        for j in range(i+1,size):
            if(li[j] <li[min_ind]):
                min_ind = j
        li[i],li[min_ind] = li[min_ind],li[i]
        print(li)


li = [60, 20, 10, 30, 50] 
print('Before sorting: ',li)
selectionsort(li)
print('After sorting: ',li)