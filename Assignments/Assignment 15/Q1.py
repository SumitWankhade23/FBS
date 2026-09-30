# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self,bid=0, bname="Unknown", price=0.0, auther="Unknown"):
        self.bid = bid
        self.bname = bname
        self.bprice = price
        self.bauther = auther

    def __del__(self):
        print(f"{self.bauther} Book auther has been destroyed")

    def ShowBook(self):
        print(f"BookID = {self.bid}\t BookName = {self.bname}\t BookPrice = {self.bprice}\t BookAuther ={self.bauther}")

b1 = Book(101,"Automic Habit",384,"James Clare")
b1.ShowBook()

b2 = Book()
b2.ShowBook()
