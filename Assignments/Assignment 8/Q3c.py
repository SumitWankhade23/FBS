# c. 1^1 + 2^2 + 3^3+ ...... n^n
def exponecialSum(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            exp = j ** i
        sum = sum + exp 
    return sum

n = int(input("Enter number: "))   
result = exponecialSum(n)
print(result)    