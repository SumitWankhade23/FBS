# 2. Write a Python program that takes a list of strings as input and
# returns a new list containing the uppercase versions of the strings
# using list comprehension.
str = input("Enter string: ")
li = [s for s in str.upper() ]
print(li)