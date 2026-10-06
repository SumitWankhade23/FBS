f = None 
try:
    f = open("abc.txt","r")
    data = f.read()
    if not data:
        raise Exception("File me kuch nahi hai")
except FileExistsError as fe:
    print(fe)    
except Exception as e:
    print(e)        
else:
    print(data)
finally:
    if f is not None:
        print("File is close")
        f.close() 
print("I am in outside ABc")       


    