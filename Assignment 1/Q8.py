#Write a program to convert days into years, weeks and days.
D = int(input("Enter days: ")) #Tota days 
Y =  D // 365 #Year 
R = D % 365 #Remaining days 

W = R % 7 #Weeks

#print("Total days: ", D)
print("Year: ", Y)
print("Week: ", W)
print("Remaining days: ", R)

