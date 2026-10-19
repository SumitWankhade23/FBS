# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero
class InvalidTelevisionData(Exception):
    pass
class Television:
    def __init__(self, model_no=0, screen_size=0, price=0):
        self.modelNo = model_no
        self.screenSize = screen_size
        self.price = price

    def accept(self):
        model_no = int(input("Enter model number (max 4 digits): "))
        screen_size = float(input("Enter screen size in inches (12 to 70): "))
        price = float(input("Enter price in Rs (0 to 5000): "))

        if len(str(abs(model_no))) > 4:
            raise InvalidTelevisionData("Model number has more than 4 digits")
        if screen_size < 12 or screen_size > 70:
            raise InvalidTelevisionData("Screen size must be between 12 and 70 inches")
        if price < 0 or price > 5000:
            raise InvalidTelevisionData("Price must be between 0 and 5000 Rs")

        # all inputs are valid, so store them
        self.modelNo = model_no
        self.screenSize = screen_size
        self.price = price

    def reset(self):
        self.modelNo = 0
        self.screenSize = 0
        self.price = 0

    def display(self):
        print("--- Television Details ---")
        print(f"Model number : {self.modelNo}")
        print(f"Screen size  : {self.screenSize} inches")
        print(f"Price        : Rs {self.price}")


def main():
    tv = Television()
    try:
        tv.accept()
    except InvalidTelevisionData as e:
        print("Error:", e)
        tv.reset()
    except ValueError:
        print("Error: please enter numbers only")
        tv.reset()
    tv.display()


if __name__ == "__main__":
    main()