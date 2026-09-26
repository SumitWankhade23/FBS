# 3. Python Program to Check if a Given key Exists in a Dictionary or Not
student = {"name": "Elon", "age": 25, "course": "Python"}

key = input("Enter key to check: ")

if key in student:
    print(f"'{key}' exists in the dictionary")
else:
    print(f"'{key}' does not exist in the dictionary")
