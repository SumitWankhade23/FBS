# 3. Count the number of spaces in a string (take input from user)
str = str(input("Enter string: "))
cnt = [s for s in str if s == " " ] 
print(len(cnt))
