class Laptop:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print(f"Company={self.company}\t Model={self.model} Price={self.price}")

l1 = Laptop("Lenovo","GX9858",100000)
l1.display()            
        