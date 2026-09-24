class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid
    def display(self):
        print(f"ID={self.id}\t Name={self.name}\t Sal={self.sal}")
    def calSal(self):
        print(f"Emp Sal = {self.sal}")
    #Str method This object super class or cosmic super class 
    #Every class is indirectly inherited from cosmic super class 
    def __str__(self):
        return f"ID={self.id}\t Name={self.name}\t Sal={self.sal}"

# Emp Ends here........................
class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com = com
    def getCom(self):
        return self.com
    def setcom(self,newcom):
        self.com = newcom
    def calSal(self):
        print(f"Fianl HR Sal = {self.com + self.getSal()}")
# Hr Ends HEre............................................
    


class Dev(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus
    def getBonus(self):
        return self.com
    def setBonus(self,newbon):
        self.bonus = newbon
    def calSal(self):
        print(f"Fianl Dev Sal= {self.bonus + self.getSal()}")
# Devoloper Ends HEre............................................

#cals sal method behaves as polymorphic behavior     
e1=Employee(12,"Sachin",900999)
h1=Hr(18,"Smriti",85669,1000)
# d=Dev(1,"Pravin",89650,100)
# e1.display()
# e1.calSal()
# h1.calSal()
# d.calSal()
print(f"Employee = {e1}")
