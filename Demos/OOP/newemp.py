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
       print(f"id={self.id}\tName={self.name}\tSal={self.sal}")
e1=Employee(12,"Sachin",1232)
e2=Employee(18,"Smriti",98989)
e1.display()
# e1.name="Viarat"
e1.setName("Virat")
e1.display()
print(e2.getSal())
e2.setSal(12121212)
print(e2.getName()," ",e2.getSal())