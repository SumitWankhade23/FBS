#10. Write a program to print list after removing even numbers.
def remov_evennum(data):
    li = []
    for i in data:
        if i % 2 != 0:
            li.append(i)
    return li

data = [1,2,3,4,5,6,7,8]
result = remov_evennum(data)
print(f"New list = {result}")
