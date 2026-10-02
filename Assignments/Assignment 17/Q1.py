# 1. Create a class Student with following
    # a. data members :
    #     i. StudentId
    #     ii. Name
    #     iii. Age
    #     iv. Percentage
    # b. Add the following methods :
    #     i. Parameterized constructor
    #     ii. Display
    #     iii. Accept
    #     iv. Method CalculateRank
    #     v. Override __str__ Method
class Student:
    def __init__(self,studentID=101,sname = "Unknown",sage = "unkown",percentage ="unkwon"):
        self.studentID = studentID
        self.name = sname
        self.age = sage
        self.percentage = percentage

    def display(self):
                print(f"StudentID = {self.studentID}\t Name = {self.name}\t Age = {self.age}\t Percentage = {self.percentage}")

    def accept(self):
        self.studentID = int(input("Enter ID: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.percentage = float(input("Enter percentage: "))      

    def calculate_rank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"      

    def __str__(self):
        return (f"StudentID={self.studentID}\t  Name={self.name}\t Age={self.age}\t " 
                f"Percentage={self.percentage}%\t  Rank={self.calculate_rank()}\t")

s1 = Student(1, "Amit", 20, 82.5)    
s1.display()
print(s1)

s2 = Student()                        
s2.accept()
s2.display()
print(s2)                  