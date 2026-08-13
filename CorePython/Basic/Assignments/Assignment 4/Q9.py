#WAP to print all numbers in a range divisible by a given number.
num = int(input("Enter number:"))
start = int(input("Enter number: "))
end = int(input("Enter number: "))

for i in range(start,end+1):
    if( i % num == 0):
        print(i, end = " ")
        