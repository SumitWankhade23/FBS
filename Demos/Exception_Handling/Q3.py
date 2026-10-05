try:
    #we are doing risky task here
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    print("Result:", num1//num2)
except ZeroDivisionError as a:
    print(f"I am zerodivtion error = {a}")
except ValueError as v:
    print(f"Value error = {v}")
except Exception as e:
    print(f"This is genralized exption it comes after all the exception becouse it block allthe exception:{e}")    
else:
    print("I am in else block ")
finally:
    print("I am in finnaly block")
  