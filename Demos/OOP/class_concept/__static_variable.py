class Student:
    inName = "FBS"

    @staticmethod
    def greet():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   

    def __init__(self,rollNo,name,batch):
        self.rollnum = rollNo
        self.nm = name
        self.batch = batch
      

    def getname(self):
        return self.nm
    def setname(self,newName):
        self.nm = newName

    def getRollnum(self):
        return self.rollnum
    def setRollnum(self,newRoll):
        self.rollnum = newRoll

    def getBatch(self):
        return self.batch
    def setNewbatch(self,newBatch):
        self.batch = newBatch

    def display(self):
        print(f"RollNo = {self.rollnum}\t Name = {self.nm}\t Batch ={self.batch}\t Institue = {self.inName}\t")  

s1 = Student(101,"Sumit","JullyPython") 
s2 = Student(102,"Sasha","JullyPython") 
s3 = Student(103,"Smita","AugustPython") 
s4 = Student(10,"Shubham","JullyPython") 
Student.greet()
s1.display()
s2.display()
s3.display() 
s4.display() 

# s1.setname("Sanju")
# s1.display()

Student.inName = "FirstSolution"



# s1.getname()
# s1.display()






        