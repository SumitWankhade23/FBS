# #1. Python Program to Add a Key-Value Pair to the Dictionary
# student = {"name": "Elon", "age": 25}
# print("Before:", student)

# key = input("Enter key to add: ")
# value = input("Enter value: ")

# student[key] = value
# print("After:", student)

def add_keyVal(d, key, val):
    d[key] = val
    return d


student = {"name": "Elon", "age": 25}
key = input("Enter key: ")
val = input("Enter value: ")
result = add_keyVal(student, key, val)
print("Student:", result)