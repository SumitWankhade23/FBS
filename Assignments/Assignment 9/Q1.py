#1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n! Note : For fact and sum two recursive functions
def fact(n):
    if( n == 0):
        return 1
    else:
        return n * fact(n-1)

def sum_series(n,sum):
    if( n == 0):
        return sum 
    else:
        sum += fact(n) 
        return sum_series(n-1,sum)

n = int(input("Enter number: "))
sum = 0
result = sum_series(n,sum)
print("Sum of factorial series: ",result)    
       