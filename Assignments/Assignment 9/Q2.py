#2. Write a program to check if given number is Armstrong or not using recursive function.
def get_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + get_digits(n // 10)


def armstrong_sum(n, x):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return digit ** x + armstrong_sum(n // 10, x)


num = int(input("Enter number: "))

x = get_digits(num)
result = armstrong_sum(num,x)

if num == result:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
