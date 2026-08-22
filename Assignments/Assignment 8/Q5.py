#5. Sum of all prime numbers between 1 to n
def sum_primeNum(num):
    sum = 0
    for i in range(2,num+1):#1 is NOT prime number
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            sum = sum + i
    return sum            
            
    
         
num = int(input("Enter number: "))
result = sum_primeNum(num) 
print(f"Sum of prime numbers upto {num} = {result}")           