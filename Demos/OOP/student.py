class Student:
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print(f"RollNumber = {self.rollno}\t Name = {self.name}\t Marks = {self.marks}")

s1 = Student(12,"Sumit",45)
s2 = Student(13,"Sudha",77)
s1.display()
s2.display()        
print(s2.rollno) 
print()   
s1.display()
s2.display()
s1.name="Rahul"
s2.marks=89
s1.display()
s2.display()

        