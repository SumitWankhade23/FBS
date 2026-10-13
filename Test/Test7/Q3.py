# 3. Write a Python program that generates a list of odd numbers from 1
# to 50 using list comprehension and filters out the even numbers
odd_numbers = [n for n in range(1, 51) if n % 2 != 0]
print(odd_numbers)