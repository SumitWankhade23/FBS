#Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)
num = int(input("Enter number: "))
count = 0
total = 0
n = num
while (n > 0):
    count += 1
    n //= 10
n = num
while( n > 0 ):
    total = total + (n%10)** count
    n //= 10
if( total == num):
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not Armstrong number")     
