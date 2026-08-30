#4. Write a program to reverse the list.
def rev_list(data):
    rev = []
    for i in range(len(data)):
        rev = [data[i]] + rev
    return rev

data = [1,2,3,4,5,6,7]
print(data)   
res = rev_list(data)
print(res) 