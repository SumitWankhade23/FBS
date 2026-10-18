from SY.symarks import SYmarks
from TY.tymarks import TYMarks
total_marks = 300

class Student:
    def __init__(self,rollNo=0,name='Unknown', symarks=0,tymarks=0):
        self.rollNo = rollNo
        self.name = name 
        self.symarks = symarks
        self.tymarks =tymarks

    def computer_total(self):
        return self.symarks.computer_total + self.tymarks.theory + self.tymarks.practical

    def percentage(self):
        return self.computer_total() / total_marks * 100   
      
    def calculate_grade(self):
        p = self.percentage()
        if p >= 70:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 50:
            return "C"
        elif p >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display(self):
        print("=" * 40)
        print("          STUDENT RESULT")
        print("=" * 40)
        print(f"Roll number        : {self.rollNo}")
        print(f"Name               : {self.name}")
        print("-" * 40)
        print(f"SY Computer        : {self.symarks.computer_total}")
        print(f"TY Theory          : {self.tymarks.theory}")
        print(f"TY Practical       : {self.tymarks.practical}")
        print("-" * 40)
        print(f"Computer total     : {self.computer_total()} / {total_marks}")
        print(f"Percentage         : {self.percentage():.2f}%")
        print(f"Grade              : {self.calculate_grade()}")
        print("=" * 40)
 
 
def main():
    try:
        rollNo = int(input("Enter roll number: "))
        name = input("Enter name: ")
        comp = float(input("Computer total (out of 100): "))
        maths = float(input("Maths total: "))
        elec = float(input("Electronics total: "))
        theory = float(input("Theory (out of 100): "))
        practical = float(input("Practical (out of 100): "))
    except ValueError:
        print("Please enter numbers only for roll number and marks.")
        return
 
    sy = SYmarks(comp, maths, elec)
    ty = TYMarks(theory, practical)
    student = Student(rollNo, name, sy, ty)
    print()
    student.display()
 
 
if __name__ == "__main__":
    main()
         