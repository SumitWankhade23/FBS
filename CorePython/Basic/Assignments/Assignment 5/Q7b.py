# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N = int(input("Enter number: "))
total = 0
for i in range(1,N+1):
    total = total + N**i
print(f"Total = {total}")        
