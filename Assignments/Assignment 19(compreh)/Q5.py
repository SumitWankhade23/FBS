# 5. Find all of the words in a string that are less than 5 letters (take input from user)
# -----------------------------------------------------------------
data = input("Enter string: ")
word = [x for x in data.split() if len(x) < 5] 
print(word)
