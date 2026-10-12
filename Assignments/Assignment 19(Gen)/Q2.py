# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10      
        n //= 10                     
    return original == rev           

def palindrome_numbers(start=1):
    n = start
    while True:                      
        if is_palindrome(n):
            yield n
        n += 1

start = int(input("Enter starting number: "))
count = int(input("How many palindromes: "))

gen = palindrome_numbers(start)
for _ in range(count):
    print(next(gen))