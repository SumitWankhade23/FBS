# Assignment on Generator

# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.
def fibo(n):
    c_unt = 0
    a,b = 1,0
    while (c_unt < n):
        yield a + b
        a,b = b, a+b
        c_unt += 1
        
n = int(input("Enter number: "))
result = fibo(n)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

     