#7. Write a program to find sum of digits of a number.
def sum_Digit(num):
    n = num
    total = 0
    while( n > 0):
        total = total + (n%10)
        n = n // 10
    return total

num = int(input("Enter number: "))
result = sum_Digit(num)
print(f"Sum of digits of number: {result}")    
