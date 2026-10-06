def decore(func):
    print("You are in decorator")
    def innerfun():
        print("Time started ")
        print("Logger added")
        func()
        print("Tiem stopped")
        print("Logger removed")
    return innerfun
def login():
    print("Loginn is done ")
x = decore(login)  
x()      
