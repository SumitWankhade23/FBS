#Q1. Write a program to find sum of all elements of list
def sum_list(data):
    sum = 0
    for i in  data:
        sum = sum + i
    return sum

data = [10,20,30,40,50,60]
result = sum_list(data)
print(f"Sum of all element of list:  {result}")    