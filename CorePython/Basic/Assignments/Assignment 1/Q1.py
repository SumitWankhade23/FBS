#Write a program to calculate the percentage of student based on marks of any 5
#subjects
Sub1 = float(input("Enter the marks of English: "))
Sub2 = float(input("Enter the marks of Hindi: "))
Sub3 = float(input("Enter the marks of Marathi: "))
Sub4 = float(input("Enter the marks Math's: "))
Sub5 = float(input("Enter the marks Science: "))


Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
maxMarks = 500
percentage = (Total/maxMarks)* 100
percentage = round(percentage, 4)

print("Percentage: ", percentage )