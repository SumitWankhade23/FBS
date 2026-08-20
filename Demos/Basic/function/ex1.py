#WAP to chech given number is palindrom or not and return the result in TRUE 
#or False
def palindrom(num):
    n = num
    rev = 0
    while( n > 0):
        rev = rev * 10 + (n%10)
        n //= 10
    if( rev == num):
        return True
    else:
        return False

num = int(input("Enter number: "))
result = palindrom(num)
print(result)
    