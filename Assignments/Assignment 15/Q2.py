# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowProduct
class Product:
    def __init__(self,pid=0,pname="Unknown",price=0,quantity="Unknwon"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__ (self):
        print(f"{self.quantity} Quantity has been destroyed")

    def ShowProducts(self):
        print(f"ProductID = {self.pid}\t Pname = {self.pname}\t Price = {self.price}\t Quantity = {self.quantity}")

p1 = Product()
p1.ShowProducts()



p2 = Product(101,"Cotton",9000,20)
p2.ShowProducts()


        

