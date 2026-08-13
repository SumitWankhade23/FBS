#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
male = int(input("Enter male age: "))
female = int(input("Enter female age: "))

if( male >= 21 and female >= 18):
    print(f"Eligible for marrage")
else:
    print(f"Not eligible for marrage")    