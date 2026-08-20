#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
English = int(input("Enter english marks: "))
Physics = int(input("Enter physics marks: "))
chem = int(input("Enetr chemistry marks: "))
Bio = int(input("Enter biology marks: "))
Maths = int(input("Enter maths marks: "))

percentage = ((English + Physics + chem + Bio + Maths)/500) * 100
print(f"Percentage = {percentage}")

if( English >= 35 and Physics >=35 and chem >= 35 and Bio >= 35 and Maths >= 35):
    if(percentage >= 75 ):
        print(f"First class with distinction")
    elif(percentage >= 65):
        print(f"First class")
    elif(percentage >=55 ):
        print(f"Second class")
    elif(percentage >= 35):
        print(f"Third class")   
else:
    print(f"Fail **You have to study hard**")    


