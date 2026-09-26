# 6. Python Program to Multiply All the Items in a Dictionary
def multiply_all(data):
    total = 1
    for i in data.values():
        total *= i
    return total

data = {"A": 10, "B":20, "C":30, "D":40, "E":50}
result = multiply_all(data)
print(result)   


