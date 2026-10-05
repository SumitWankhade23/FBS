from myexception import MyException
try:
    age = int(input("Enter the age: "))
    if age <= 0:
        #raise ZeroDivisionError("Enter valid age")
        raise MyException

except MyException as m:
    print

except Exception as e:
    print(e)
