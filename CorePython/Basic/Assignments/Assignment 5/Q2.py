# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
students = int(input("Enter number students: "))
n = students
total_percentage = 0

for i in range(1,n+1):
    total_marks = 0
    print(f"Enter marks of the students {i}")
    for j in range(1,6):
        marks = int(input("Enter marks: "))
        total_marks += marks
    percentage = (total_marks/500) * 100 

    total_percentage += percentage

avergae = total_percentage/ n
print(f"Average percentage = {avergae} %")
