#Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter principle: "))
T = float((input("Enter time: ")))
R = float(("Enetr the rate: "))

SI = (P*T*R) / 100

Total = P + SI

print("Expected Smiple interest will be:", SI)
print("Total amount:", Total )
