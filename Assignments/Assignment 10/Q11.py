#Write a program to print all numbers which are divisible by m and n in the list.
def print_divisible_numbers(numbers, m, n):
    result = []
    for num in numbers:
        if num % m == 0 and num % n == 0:
            result = result + [num]
    
    for num in result:
        print(num,end=" ")
    
    return result

numbers = [10, 15, 20, 24, 30, 35, 40, 45, 50, 60]
m = int(input("Enter number: "))
n = int(input("Enter number: "))

print(f"Numbers divisible by {m} and {n}:")
print_divisible_numbers(numbers, m, n)


