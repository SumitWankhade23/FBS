#Python Program to Find the Union of two Lists
def find_Union(data1,data2):
    union_list = []
    for i in data1:
        if i not in union_list:
            union_list.append(i)

    for i in data2:
        if i not in union_list:
            union_list.append(i)
    return union_list

data1 = [1,3,5,7,9]
data2 = [2,4,6,8,10,1,3,5]
result = find_Union(data1,data2)
print(f"data1 = {data1}")
print(f"data2 = {data2}")
print(f"Union of data1 and data2 : {result}")        
