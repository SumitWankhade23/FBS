#seperateout digits using recursive function
def separte_digit(n):
    if n == 0:
        return 
   
    separte_digit(n//10)
    d = n % 10
    print(d)

n = int(input("Enter number: "))
res = separte_digit(n)

