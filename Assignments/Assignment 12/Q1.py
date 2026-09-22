#1. Python Program to Replace all Occurrences of ‘a’ with $ in a dataing
def replace_occ(data):
    new_data = ""
    for i in data:
        if( i == 'a'):
            new_data = new_data + '$'
        else:
            new_data = new_data + i
    return new_data

data = "Sanjana " 
result = replace_occ(data)
print(result)       