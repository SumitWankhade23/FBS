#Write a program to create three lists of numbers, their squares and cubes
def create_list(data):
    sq_list = []
    cb_list = []
    new_list = []
    for i in range(len(data)):
        sq_list = sq_list + [data[i]**2]
        cb_list = cb_list + [data[i]**3]
        new_list = new_list+ [data[i]]
    return sq_list,cb_list,new_list    
data = [2,3,4,5,6,7,8,9]
result = create_list(data)
print(f"Squre list = {result[0]}")
print(f"cub list = {result[1]}")
print(f"Squre list = {result[2]}")
