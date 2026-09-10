#Write a program to create a duplicate of an existing list. It should not point to same list.
def duplicate_list(data):
    new_List = []
    for i in range(len(data)):
        new_List = new_List + [data[i]] 

    return new_List  
data = [10,20,30,40,50,50]
result = duplicate_list(data)
print("Old_List",data)
print("New_List",result)  
