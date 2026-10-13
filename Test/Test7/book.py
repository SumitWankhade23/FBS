# 1. Using Modules concept
# Create a class to store book details (bid, name, price and author).
# Write a menu driven program with following options:
    # a. Add Book
    # b. Delete book by id
    # c. Display all books
    # d. Search book by id
    # Use dictionary to store all information.
class StoreBook:
    book = {}
    def __init__(self,bid="Unknown",bname="Unknown",price=0,auther="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.auther = auther

    
    def display(self):
        print(f"Book id= {self.bid}")
        print(f"Book name = {self.bname}")
        print(f"Book price = {self.price}")
        print(f"Auther = {self.auther}")

    
    def __str__(self):
        print(f"Book id ={self.bid}\t Book name = {self.bname}\t Book price ={self.price}\t Auther name = {self.auther}")




            