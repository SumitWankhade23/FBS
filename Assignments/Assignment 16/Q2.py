# 2. Create a class Product with members as pid,pname,price and quantity .Add
#    following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.
class Book:
    count = 0   
    def __init__(self, bid=0, bname="Unknown", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1          


    def __del__(self):
        print(f"Destructor called: book '{self.bname}' removed")

    
    def show_book(self):
        print("--- Book Details ---")
        print(f"ID     : {self.bid}")
        print(f"Name   : {self.bname}")
        print(f"Price  : {self.price}")
        print(f"Author : {self.author}")



b1 = Book()                                           
b2 = Book(101, "Python Basics", 450.50, "Guido")      
b3 = Book(102, "Data Structures", 600, "Mark")

b1.show_book()
b2.show_book()
b3.show_book()

print("Total books created:", Book.count)

del b2      
print("End of program")
