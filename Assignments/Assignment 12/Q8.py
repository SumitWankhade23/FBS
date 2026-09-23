#8. Python Program to Remove the Characters of Odd Index Values in a
#   String
def rem_oddindexchar(text):
    new_text = ""
    for i in range(len(text)):
        if i %2 == 0:
            new_text += text[i]
    return new_text

text = "Sumit"
result = rem_oddindexchar(text)
print(result)    

#Two approch 
def rem_oddindexchar(text):
    return text[::2] 
  
print(rem_oddindexchar("Elon"))
