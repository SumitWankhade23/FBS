def infiniteValue_gen():
    i = 1
    while(True):
        yield i
        i += 1

res = infiniteValue_gen()
print(next(res))
print(next(res)) 
print(next(res)) 
print(next(res))
print(next(res)) 
print(next(res))
print(next(res))
print(next(res)) 
print(next(res))         