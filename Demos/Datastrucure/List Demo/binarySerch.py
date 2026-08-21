def binarySearch(ele,li):
    beg = 0
    end = len(li)-1
    while( beg <= end):
        #print('beg: ', beg)
        #print('end: ', end)
        mid = (beg+end)//2
        #print('mid:',mid)
        #print('search_Element: ',ele)
        #print('mid ele:', li[mid])
        if(ele == li[mid]):
            return mid
        elif(ele < li[mid]):
            #print('Less than)
            end = mid - 1
        elif(ele > li[mid]):
            #print('greater than)
            beg = mid +1

    else:
        return -1              

ele = int(input("Enter element to be search: "))
li = [10,20,30,40,50,60]
res = binarySearch(ele,li)
#print(res)
if(res != -1):
    print(f"{ele} is found at index {res}")
else:
    print(f"{ele} is not found ")