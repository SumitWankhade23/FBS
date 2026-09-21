#1. For memory optimization 
#2. Genrating value according to user requirement
#3. Use yield key
#4. Maitain state(Maintain stack frame) of function 
#5. Iterating upcoming value using next from iterable         

def genratevalues(n):
    for i in range(1,11):
        yield i

result = genratevalues(4)
print(next(result))  
print(next(result)) 
print(next(result)) 
print(next(result))       
