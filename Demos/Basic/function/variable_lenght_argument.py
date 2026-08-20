#1.To pass multiple values to the function
#2. Menstion 1 asterisk symbol before parameter name in function defination
#3. Passed value storec in tuple format 
#4. Use for loop to iterate value from tuple

def add(*data):
    print('add function call')
    print(type(data))
    sum = 0
    for val in data:
        sum = sum + val
    return sum    

result = add(10,20,30,20,4,10,25,25,45,46,25,75,84,85,55) 
print(result)   