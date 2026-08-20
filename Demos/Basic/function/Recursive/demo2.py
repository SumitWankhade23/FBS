def series(n):
    if(n > 0):
        print(n)
        series(n-1)

n = int(input("Enter number: "))
series(n)