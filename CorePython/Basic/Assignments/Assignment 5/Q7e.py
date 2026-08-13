# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
n = int(input("Enter terms: "))
x = int(input("Enter number: "))

Result  = 0
for i in range(1,n+1):
    terms = (x ** i)/(2*i-1)
    if(i%2 == 0):
        Result = Result - terms
    else:
        Result = Result + terms
print(f"Result= {Result}")            