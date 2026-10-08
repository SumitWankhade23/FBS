#WAP to create  class of Employee and add  the emp object into  a file
import pickle
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
        print(f"ID = {self.id}")
        print(f"Name = {self.nm}")
        print(f"Salary = {self.sal}")

    def __str__(self):
        return f"\n{self.id} {self.nm} {self.sal}" 
         
                 

e1 = Employee(101,"Sumit",50000)
e2 = Employee(102,"Sachin",30000)
e3 = Employee(103,"Sam",70000)



# with open("abc.txt",'w') as fw:
#     fw.write(str(e1))
#     fw.write(str(e2))
#     fw.write(str(e3))
    

# with open("abc.txt",'r') as fr:
#     data = fr.read()
#     print(data)
#     e1= data.split()
#     #e1.setName("Rahul") You can not set name directly with this method
#     print(e1)
#     eid = int(data[0])
#     name = (data[1])
#     sal = (data[2])
#     emp = Employee(eid,name,sal)
#     emp.setName("Rahul")
#     print(emp)

f = open("emp.dat","wb") #This file is not readable 
#pickle.dump("ObjectName","ObjectOfFile")
pickle.dump(e1,f)


f = open("emp.dat","rb")
print(f.tell())
data = pickle.load(f)
print(data)
print(data.getName())



        