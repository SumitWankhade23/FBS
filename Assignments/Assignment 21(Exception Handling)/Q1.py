# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.
class InvalidOperatorError(Exception):
    pass
class Calculator:
    def __init__(self, val_1=0, val_2=0):
        self.val_1 = val_1
        self.val_2 = val_2
        self.operator = ""
        self.result = 0

    def addition(self):
        return self.val_1 + self.val_2

    def subtract(self):
        return self.val_1 - self.val_2

    def multi(self):
        return self.val_1 * self.val_2

    def division(self):
        return self.val_1 / self.val_2         

    def calculate(self, operator):
        self.operator = operator
        if operator == "+":
            self.result = self.addition()
        elif operator == "-":
            self.result = self.subtract()
        elif operator == "*":
            self.result = self.multi()
        elif operator == "/":
            self.result = self.division()
        else:
            raise InvalidOperatorError(f"'{operator}' is not a valid operator. Use + - * /")
        return self.result


    def __str__(self):
        return (f"{self.val_1} {self.operator} "
                f"{self.val_2} = {self.result}")


def main():
    try:
        val_1 = float(input("Enter first number : "))
        val_2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()

        calc = Calculator(val_1, val_2)
        calc.calculate(operator)
        print("Result:", calc)

    except ValueError:
        print("Error: Invalid number. Please enter digits only (for example 12 or 3.5).")
    except InvalidOperatorError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        print("Calculation finished.")


if __name__ == "__main__":
    main()