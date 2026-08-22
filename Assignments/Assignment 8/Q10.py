#10. Write a program to check if entered year is a leap year or not.
def check_leap_year(year):
    if year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    elif year % 4 == 0:
        return True

    else:
        return False
    
year = int(input("Enter year: "))
result = check_leap_year(year)
if( result == True):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")       
            
