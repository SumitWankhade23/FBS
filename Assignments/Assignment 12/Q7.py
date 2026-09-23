#7. Python Program to Calculate the Length of a String Without Using a
#   Library Function
def cal_Lenstring(text):
    count = 0
    for char in text:
        count += 1
    return count

text = "Firsthbit solution"
result = cal_Lenstring(text)
print(result)        
            
