#1. Write a program to accept year from user and check if it is a leap year or not.
def leap_year(year):
    if year%400 == 0:
        return True
    elif(year%100 == 0):
        return False
    elif(year%4 == 0):
        return True
    else:
        return False

year = int(input("Enter year: "))
result = leap_year(year)
print(result)    