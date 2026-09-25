# 12. Python Program to count number of lowercase characters in a string.
def count_lowercase(text):
    count = 0
    for ch in text:
        if 'a' <= ch <= 'z':
            count += 1
    return count

text = str(input("Enter string: "))
result = count_lowercase(text) 
print(result)       

