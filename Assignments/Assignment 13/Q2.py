#2. Python Program to Concatenate Two Dictionaries Into One
def concatenate(dict1,dict2):
    new_dict = dict1.copy()
    for a,b in dict2.items():
        new_dict[a] = b
    return new_dict    

dict1 = {"Name" : "Sumit", "Age": 25, "Height": 5.5}
dict2 = {"Addrees": "Kapustalni", "Roll": 101}
result = concatenate(dict1,dict2)
print(result)

