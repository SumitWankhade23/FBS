#with passing paramter
#with returning value
def addition(num1,num2):

    add = num1 + num2

    return add

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
result = addition(num1,num2)
print(f"Addition = {result}")