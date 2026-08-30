#7. Write a program to create a new list from existing list which contains cube of each number of list.
def cub_function(data):
    new_list = []
    for i in range(len(data)):
        new_list = [data[i]**3] 
    return new_list

data = [1,2,3,4,5]
print(data)
result = cub_function(data)
print(result)    