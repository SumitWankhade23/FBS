#Write a program to create three lists of numbers, their squares and cubes
def create_list(data):
    squr_list = []
    cub_list = []
    for i in data:
        squr_list.append(i**2)
        cub_list.append(i**3)

    return squr_list,cub_list
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = create_list(data)
print(f"List = {data}")
print(f"Squre list = {result[0]}")
print(f"Cube list = {result[1]}")    
