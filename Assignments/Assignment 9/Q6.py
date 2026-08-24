#6. Write a program to print Fibonacci series using recursion.
def fibo_series(a,b,n):
    if(n == 0):
        return 
    else:
        c = a + b 
        print(c, end=" ")
        fibo_series(b,c, n-1)

n = int(input("Enter number: "))
fibo_series(1,0,n)