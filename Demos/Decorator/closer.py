def decore(a):
    # print("I am in decorer")
    def innerfun(*args):
        print("Time started ")
        print("Logger added")
        a(*args)
        print("Time Stopeed")
        print("Logger removed ")
    return innerfun 
@decore
def login():
    print("Log in is Done")
    
@decore
def logout():
    print("Logout in is Done")

@decore
def add(a,b):
    print(f"Addition ={a+b}")

add(12,23)

# res=decore(login)
# res()

login()
#logout()