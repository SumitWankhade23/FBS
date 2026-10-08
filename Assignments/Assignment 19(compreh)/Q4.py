# 4. Remove all of the vowels in a string (take input from user)
text = input("Enter text: ")
result = "".join([s for s in text if s.lower() not in "aeiou"])
print(result)