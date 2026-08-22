#4. Sum of all odd numbers between 1 to n
def Odd_numSum(num):
    sum = 0
    for i in range(1,num+1):
        if(i%2 != 0):
            sum += i
    return sum

num = int(input("Enter number: "))
result = Odd_numSum(num)
print(f"Sum of odd numbers = {result}")        