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
# 2. Create a derived class from Student as EnggStudent with :
#     a. Data members as :
#         i. Branch
#         ii. InternalMarks
#     b. Add the following methods :
#         i. Parameterized constructor
#         ii. Display
#         iii. Accept
#         iv. override Method CalculateRank
#         v. Override __str__ Method
# 3. Create a class MedicalStudent inherited from Student with following:
    #a. 
        # i. Data members :Specialization
        # ii. MarksOfInternship
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. override Method CalculateRank
        # v. Override __str__ Method
# 4. Create a class College which has collection of students.
#  Add the following methods :
    # a. Parameteried constructor for number of students.
    # b. AddStudent
    # c. GetStudent
    # d. RemoveStudent
    # e. Override __str__ Method
      
# ---------------------------------------------------------------
# 1. Base class: Student
# ---------------------------------------------------------------
class Student:
    # i. Parameterized constructor
    def __init__(self, student_id=0, name="Unknown", age=0, percentage=0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    # iii. Accept
    def accept(self):
        self.student_id = int(input("Enter student id: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.percentage = float(input("Enter percentage: "))

    # ii. Display
    def display(self):
        print("--- Student Details ---")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Percentage : {self.percentage}%")
        print(f"Rank       : {self.calculate_rank()}")

    # helper: convert a score into a rank category
    @staticmethod
    def rank_from_score(score):
        if score >= 75:
            return "Distinction"
        elif score >= 60:
            return "First Class"
        elif score >= 50:
            return "Second Class"
        elif score >= 40:
            return "Pass Class"
        return "Fail"

    # iv. CalculateRank
    def calculate_rank(self):
        return Student.rank_from_score(self.percentage)

    # v. Override __str__
    def __str__(self):
        return (f"Student[ID={self.student_id}, Name={self.name}, Age={self.age}, "
                f"Percentage={self.percentage}%, Rank={self.calculate_rank()}]")


# ---------------------------------------------------------------
# 2. Derived class: EnggStudent
# ---------------------------------------------------------------
class EnggStudent(Student):
    # i. Parameterized constructor
    def __init__(self, student_id=0, name="Unknown", age=0, percentage=0.0,
                 branch="Unknown", internal_marks=0.0):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks      # out of 100

    # iii. Accept
    def accept(self):
        super().accept()
        self.branch = input("Enter branch: ")
        self.internal_marks = float(input("Enter internal marks (out of 100): "))

    # ii. Display
    def display(self):
        super().display()
        print(f"Branch     : {self.branch}")
        print(f"Internal   : {self.internal_marks}")

    # iv. Override CalculateRank: 70% percentage + 30% internal marks
    def calculate_rank(self):
        score = 0.7 * self.percentage + 0.3 * self.internal_marks
        return Student.rank_from_score(score)

    # v. Override __str__
    def __str__(self):
        return (f"EnggStudent[ID={self.student_id}, Name={self.name}, Age={self.age}, "
                f"Percentage={self.percentage}%, Branch={self.branch}, "
                f"Internal={self.internal_marks}, Rank={self.calculate_rank()}]")


# ---------------------------------------------------------------
# 3. Derived class: MedicalStudent
# ---------------------------------------------------------------
class MedicalStudent(Student):
    # i. Parameterized constructor
    def __init__(self, student_id=0, name="Unknown", age=0, percentage=0.0,
                 specialization="Unknown", internship_marks=0.0):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.internship_marks = internship_marks  # out of 100

    # iii. Accept
    def accept(self):
        super().accept()
        self.specialization = input("Enter specialization: ")
        self.internship_marks = float(input("Enter internship marks (out of 100): "))

    # ii. Display
    def display(self):
        super().display()
        print(f"Speciality : {self.specialization}")
        print(f"Internship : {self.internship_marks}")

    # iv. Override CalculateRank: 60% percentage + 40% internship marks
    def calculate_rank(self):
        score = 0.6 * self.percentage + 0.4 * self.internship_marks
        return Student.rank_from_score(score)

    # v. Override __str__
    def __str__(self):
        return (f"MedicalStudent[ID={self.student_id}, Name={self.name}, Age={self.age}, "
                f"Percentage={self.percentage}%, Specialization={self.specialization}, "
                f"Internship={self.internship_marks}, Rank={self.calculate_rank()}]")


# ---------------------------------------------------------------
# 4. College: collection of students
# ---------------------------------------------------------------
class College:
    # a. Parameterized constructor (number of students = capacity)
    def __init__(self, number_of_students=10):
        self.capacity = number_of_students
        self.students = []

    # b. AddStudent
    def add_student(self, student):
        if len(self.students) >= self.capacity:
            print(f"College is full (capacity {self.capacity}). Cannot add {student.name}.")
            return False
        if self.get_student(student.student_id) is not None:
            print(f"Student id {student.student_id} already exists.")
            return False
        self.students.append(student)
        print(f"Added: {student.name}")
        return True

    # c. GetStudent (search by id)
    def get_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    # d. RemoveStudent (by id)
    def remove_student(self, student_id):
        s = self.get_student(student_id)
        if s is None:
            print(f"No student found with id {student_id}.")
            return False
        self.students.remove(s)
        print(f"Removed: {s.name}")
        return True

    # e. Override __str__
    def __str__(self):
        header = f"College ({len(self.students)}/{self.capacity} students)"
        if not self.students:
            return header + "\n  (no students)"
        return header + "\n" + "\n".join("  " + str(s) for s in self.students)



if __name__ == "__main__":
    college = College(4)

    college.add_student(Student(1, "Amit", 20, 82.5))
    college.add_student(EnggStudent(2, "Neha", 19, 68, "Computer", 85))
    college.add_student(MedicalStudent(3, "Ravi", 21, 72, "Cardiology", 90))
    college.add_student(Student(1, "Duplicate", 22, 50))      
    college.add_student(Student(4, "Sara", 20, 38))
    college.add_student(Student(5, "Extra", 20, 60))          

    print("\n", college, sep="")

    print("\nGetStudent(2):")
    found = college.get_student(2)
    if found:
        found.display()

    print("\nRemoving id 3 and id 99:")
    college.remove_student(3)
    college.remove_student(99)

    print("\n", college, sep="")                       
                 
