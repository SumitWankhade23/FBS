#Python Program to Find the Intersection of Two Lists
def intersec(data1,data2):
    intersec_list = []
    for i in data1:
        if i in data2 and i not in intersec_list:
            intersec_list.append(i)

    return intersec_list

data1 = [1,3,5,7,9,1]
data2 = [2,4,6,8,10,1,3,5]
result = intersec(data1,data2)
print(f"data1 = {data1}")
print(f"data2 = {data2}")
print(f"Intersection of data1 and data2 : {result}")  
