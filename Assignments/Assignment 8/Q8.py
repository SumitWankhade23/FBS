#8. Write a program find reverse of a number
def rev_Number(num):
    n = num
    rev = 0
    while(n > 0):
        rev = rev * 10 + (n%10)
        n = n // 10
    return rev

num = int(input("Enter number: "))
result = rev_Number(num)
print(f"Reverse of number: {result}")

