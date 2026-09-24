class Student:
    inName = "FBS"
    stuCount = 0
    def __init__(self,rollNo,name,batch):
        self.rollnum = rollNo
        self.nm = name
        self.batch = batch
        Student.stuCount += 1

    def setRollnum(self,newRoll):
        self.rollnum = newRoll 
    def getRollnum(self):
            return self.rollnum     
    def getname(self):
        return self.nm
    def setname(self,newName):
        self.nm = newName
    def getBatch(self):
        return self.batch
    def setNewbatch(self,newBatch):
        self.batch = newBatch

    def display(self):
        print(f"RollNo = {self.rollnum}\t Name = {self.nm}\t Batch ={self.batch}\t Institue = {self.inName}\t ")  

class PlacedStudent(Student):
    def __init__(self, rollNo, name, batch,cName):
        super().__init__(rollNo, name, batch)
        self.cName= cName

    def display(self):
        print(f"CName={self.cName}")
        return super().display()

s1 = Student(12,"Suraj",1234)
s2 = PlacedStudent(1,"Shankar",1232,"GlobalPayment")
print(Student.stuCount)

        
