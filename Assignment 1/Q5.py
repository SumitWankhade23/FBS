#Write a program to enter P, T, R and calculate Compound Interest
P = float(input("Enter principle amount: "))
T = float((input("Enter time: ")))
R = float(input("Enetr the rate: "))

A = P * (1 + R/100) ** T

CI = A - P 

print("Compound Interest: ", CI)

