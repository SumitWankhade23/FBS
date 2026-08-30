#6. Write a program to remove duplicates from the list.
def remove_duplicates(data):
    new_data = []
    i = 0
    while i < len(data):
        j = 0
        found = False
        while j < len(new_data):
            if data[i] == new_data[j]:
                found = True
                break
            j += 1
        if found == False:
            new_data = new_data + [data[i]]
        i += 1
    return new_data

data = [10, 20, 30, 20, 20, 20, 40, 50, 60, 70]
print("Original list:", data)
result = remove_duplicates(data)
print("List after removing duplicates:", result)