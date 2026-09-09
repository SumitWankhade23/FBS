class Bank:
    def __init__(self,accntno,name,type):
        self.accnt = accntno
        self.name = name
        self.type = type
       

    def display(self):
        print(f"Account numb = {self.accnt}\t Name = {self.name}\t Type of acc = {self.type}\t ") 

c1 = Bank(4235,"Sumit","Saving")
c1.display()