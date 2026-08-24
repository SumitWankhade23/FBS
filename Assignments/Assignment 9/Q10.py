#10. Write a program to reverse a number using recursion.
def reverse_num(n, rev):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + (n % 10)
        return reverse_num(n // 10, rev)


num = int(input("Enter number: "))
rev = 0
result = reverse_num(num, rev)

print(f"Reverse of {num} = {result}")