#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def check_Armstrong(num):
    n = num 
    rev = 0
    count = 0
    while( n > 0):
        count = count + 1
        n = n // 10
    n = num
    while(n > 0):
        rev = rev + (n%10)**count
        n = n // 10

    if num == rev:
        return True
    else:
        return False

num = int(input("Enter number: "))
result = check_Armstrong(num)
if result:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not Armstrong number")        
