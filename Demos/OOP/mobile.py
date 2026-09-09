class Mobile:
    def __init__(self,brand,price,model):
        self.brand = brand
        self.price = price
        self.model = model

    def display(self):
        print(f"BrandName : {self.brand}\t Price : {self.price}\t Model : {self.model}")

m1 = Mobile("Sony",34000,"SX4")
m2 = Mobile("MOTOROLLA",60000,"C2")
m3 = Mobile("Apple",134000,"iPhone17maxpro")
m4 = Mobile("OPPO",24000,"S1")
m5 = Mobile("Samsung",150000,"GalaxyUltra")
m1.display()
m2.display()
m3.display()
m4.display()
m5.display()

