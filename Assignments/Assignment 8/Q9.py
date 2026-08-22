#9. Write a program to check if entered number is a palindrome or not.
def rev_Number(num):
    n = num
    rev = 0
    while(n > 0):
        rev = rev * 10 + (n%10)
        n = n // 10
    return rev

num = int(input("Enter number: "))
result = rev_Number(num)
if (num == result):
    print(f"{num} is palindrom number")
else:
    print(f"{num} is not palindrom number")    

