class Car:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print(f"Company={self.company}\t Model={self.model}\tPrice={self.price}")

c1 = Car("Tata","Safari",1400000)
c1.display()            