# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = int(input("Enter number: "))
s = 0
for i in range(1,11):
    s = s + (a**i)/i

print(f"S = {s:.2f}")    
