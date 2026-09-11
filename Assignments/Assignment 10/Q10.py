#Write a program to remove all occurrences of a given element in the list.
def remove_element(data, n):
    new_data = []

    for i in range(len(data)):
        if data[i] != n:
            new_data = new_data + [data[i]]

    return new_data


data = [10, 20, 20, 30, 40, 20, 50, 20, 60]
print("Original List:", data)

n = int(input("Enter element to be removed: "))
result = remove_element(data, n)
print("New List:", result)
