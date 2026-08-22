# b. 1!+ 2! + 3! + 4!+..... + n!
def sumFact(num):
    sum = 0
    for i in range(1,num+1):
        fact = 1
        for j in range(1,i+1):
            fact = fact * j
        sum = sum + fact
    return sum    

num = int(input("Enter number: "))
result = sumFact(num)
print(result)