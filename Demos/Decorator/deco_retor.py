# def demo():
#     print("I am in demo")
# #print(type(demo))
# # a = 10 
# # print(type(a))
# x = demo
# x()  

# def outerFun():
#     print("I am in out func")
#     def innerFunc():
#         print("I am in inner func")
#     return innerFunc

# x = outerFun()
# #print(x)
# x()

def outerFun():
    a = "Virat"
    def innerFunc():
        print(a)#"Virat is pass just due to function of closer"
    return innerFunc

x = outerFun()
x()       