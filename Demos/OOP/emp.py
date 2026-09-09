class Employee:
    def __init__(self,ID,name,salary):
        self.id = ID
        self.nm = name
        self.sal = salary

    def getName(self):
        return self.nm   
    def setName(self,newName):
        self.nm = newName 

    def getSal(self):
        return self.sal
    def setSal(self,newSal):
        self.sal = newSal

    def getid(self):
        return self.id
    def setid(self,newID):
        self.id = newID        

    def display(self):
        print(f"ID = {self.id}\t Name = {self.nm}\t Salary = {self.sal}")

e1 = Employee(101,"Sumit",70000)
e2 = Employee(102,"Sagar",50000)
e3 = Employee(103,"Sushil",100000)
e1.display()
e2.display()
e3.display()
e1.setName("Virat")
e1.display()
        