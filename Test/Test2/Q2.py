# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.
num = int(input("Enter number: "))
x = num%10
y = num//10
z = y%10            
a = y//10           
if a == 2 * z and a == x*0.5 :
    print("Yes, you have done it")
else:
    print("Prease try next time")    