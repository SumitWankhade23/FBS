#The filter() function in Python is used to select elements 
# from a sequence based on a condition.
data = [1,2,3,4,5,6,7,8,9]

res = list(filter(lambda num: num%2 == 0,data))
print(res)