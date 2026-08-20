#Write a program to input angles of a triangle and check whether triangle is valid or not.
a1 = float(input("Enter angle1: "))
a2 = float(input("Enter angle2: "))
a3 = float(input("Enter angle3: "))

if( a1>0 and a2>0 and a3>0 and (a1 + a2 + a3) == 180):
    print(f"Valid triangle")
else:
    print(f"Invalid triangle")    
