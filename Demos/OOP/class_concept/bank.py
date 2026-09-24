class Bank:
    IFSC_No = "SBIN0023"
    def __init__(self,accntno,name,type):
        self.accnt = accntno
        self.name = name
        self.type = type

    def getName(self):
        return self.name   
    def setName(self,newName):
        self.name = newName 
    
    def gettype(self):
        return self.type
    def setSal(self,newType):
        self.sal = newType
    
    def getAccnt(self):
        return self.accnt
    def setid(self,newAccnt):
        self.id = newAccnt           

    def display(self):
        print(f"Account numb = {self.accnt}\t Name = {self.name}\t Type of acc = {self.type}\t IFCS={self.IFSC_No} ") 

c1 = Bank(4235,"Sumit","Saving")
c2 = Bank(4236,"Sanju","Saving")
c3 = Bank(4237,"Smita","current")
#c1.display()

#Bank.IFSC_No = "SBIN00021"
c1.display()
c2.display()
c3.display()

c1.getAccnt()
c1.display()