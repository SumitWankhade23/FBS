# 7. Python Program to Remove the Given Key from a Dictionary
def remove_key(student,key):
        if key in student:
            del student[key]
            print("Output:", student)
        else:
            print(f"'{key}' not found in the dictionary")

student = {"Name": "Virat", "Salary":125000, "Age": 35, "company": "HCL"}
key = input("Enter key to remove: ")
remove_key(student,key)
