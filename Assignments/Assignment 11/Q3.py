#Python Program to Sort the List According to the Second Element in Sublist
data = [[1,50],[2,20],[3,40],[4,10]]
data. sort(key=lambda x:x[1])
print(data)

##Without Lambda 
def second_element(x):
    return x[1]
data =  [[1,50],[2,20],[3,40],[4,10]] 
data.sort(key=second_element)
print(data)
