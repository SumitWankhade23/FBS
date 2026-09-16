class Emp:
    def __init__(self,nm):
        self.name=nm
    def display(self):
        print("Display ")
# Emp ends here....
class Devloper(Emp):
        def display(self):
            print("Disply of Dev")
# Dev ends here....
class HR(Emp):
    def display(self):
        print("disply of Hr")
#hr ends here................
class JrHR(HR):
    def display(self):
        print("I am from disply of Jr Hr")
# JR hR ENDS HERE...................
class SrHR(HR):
    def display(self):
        print("I am from disply of Sr Hr")
# SR hR ENDS HERE...................\\
class JrDev(Devloper):
    def display(self):
        print("I am from Jr Devoper")
# h1=HR("sACHIN")
# h1.display()
# s1=Emp("jdjd")
# s1.display()
jhr=JrHR("Smriti")
jhr.display()
jrd=JrDev("Sachin")
jrd.display()