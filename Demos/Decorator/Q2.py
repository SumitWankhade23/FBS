##Understand that your function is nothing but object of function class
# def demo():
#     print("I am in demo")

# x= demo
# x()

## We can store the function in variable
# def demo(a):
#     a()

# def fun():
#     print("I am in tested function")
# demo(fun)  

##Return one function from other function
def outerfun():
    print("I am in outer")
    def innerfunc():
        print("i am in inner function") 
    return innerfunc
result = outerfun()
result()     