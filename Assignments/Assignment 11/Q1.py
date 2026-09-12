#1. Python Program to Put Even and Odd elements of a List into two Different Lists
def diff_list0(data):
    odd_list = []
    even_list = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            even_list.append(data[i])
        else:
            odd_list.append(data[i])   
    return even_list,odd_list
data = [1,2,3,4,5,6,7,8,9,10]
result = diff_list0(data)
ProcessLookupError
print(f"Original List = {data}")
print(f"Even List = {result[0]}")
print(f"Odd list = {result[1]}")        
