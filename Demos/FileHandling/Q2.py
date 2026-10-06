f = None 
try:
    f = open("abc.txt","r")
    data = f.read()
except Exception as e:
    print(e)        
else:
    print(data)
finally:
    if f is not None:
        print("File is close")
        f.close() 
print("I am in outside ABc")       


    