#WAP to print Armstrong number within a given range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):

    n = num
    count = 0
    total = 0

    while (n > 0):
        count += 1
        n = n//10
    n = num
    while(n > 0):
        total = total + (n%10)**count
        n = n // 10

    if( num == total):
        print(f"{num} is Armstrong number")
    
