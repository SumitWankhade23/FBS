import sys

try:
    num = int(input("Enter a number: "))
    print(10 // num)
except ValueError:
    print("Invalid input. Exiting.")
    sys.exit(1)
except ZeroDivisionError:
    print("Cannot divide by zero. Exiting.")
    sys.exit(1)