# 5. Python Program to Sum All the Items in a Dictionary
def sum_all(data):
    total = 0
    for i in data.values():
        total += i
    return total

data = {"A": 10, "B":20, "C":30, "D":40, "E":50}
result = sum_all(data)
print(result)   

