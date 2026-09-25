# 11. Python Program to replace every blank space with hyphen in a string.
def replace_blank(data):
    new_data = ""
    for ch in data:
        if ch == " ":
            new_data += "-"
        else:
            new_data += ch
    return new_data

data = "Elon musk has X"
result = replace_blank(data)
print(result)            
