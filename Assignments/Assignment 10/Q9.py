#Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
def check_num(data):
    even_num = []
    odd_num = []
    for i in range(len(data)):
        if data[i]%2 == 0:
            even_num = even_num + [data[i]]
        else:
            odd_num = odd_num + [data[i]]
    return odd_num, even_num        


data = [11,2,3,4,5,6,4,7,8,78,25]
result = check_num(data)
print(f"Odd NUm List {result[0]}")
print(f"Even NUm List {result[1]}")
