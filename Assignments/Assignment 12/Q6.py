#6. Python Program to Take in a String and Replace Every Blank Space
#   with Hyphen
def reap_string(text):
    result = ""
    for char in text:
        if char == " ":
            result += "-"
        else:
            result +=  char
    return result

text = "Mere Brother Ki Dulhan"
new_text = reap_string(text)
print(new_text)            

 
#shortest version 
# text = "Mere brother ki dulhan"
# new_text = text.replace(' ', '-')
# print(new_text)    
