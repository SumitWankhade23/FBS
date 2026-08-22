# #6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacciSeries(n):
    a,b = 1,0
    i = 0
    while( i <= n):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
        i += 1      
    
n = int(input("Enter number: "))
fibonacciSeries(n)



        

