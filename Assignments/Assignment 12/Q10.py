# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
def string_length(text):
    count = 0
    for char in text:
        count += 1
    return count

def Larger_string(text1,text2):
    Len1 = string_length(text1) 
    Len2 = string_length(text2) 
    if Len1 > Len2:
        print(f"FirstString = {text1} is Larger string")
    elif Len2 > Len1:
        print(f"SecondString = {text2} is Larger string")
    else:
        print(f"text1 and text2 are equal length string")
        

text1 = str(input("Enter string1: ")) 
text2 = str(input("Enter string2: "))
Larger_string(text1,text2)
  


