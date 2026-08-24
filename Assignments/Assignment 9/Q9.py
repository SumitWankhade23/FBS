#9. Write a program to calculate the m to the power n using recursion.
def calculate_power(m,n):
    if(m < 0):
        return 0
    elif(n == 0):
        return 1
    else:
        return m * calculate_power(m,n-1)

m = int(input("Enter base: ")) 
n = int(input("Enter power: "))    
result = calculate_power(m,n)
print(f"{m} ** {n} = {result}")