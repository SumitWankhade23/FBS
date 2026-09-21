class A:
    def add(self):
        print("Add A")
class B:
    def add(self):
        print("Add B")
class C(B,A):
    #def __init__(self,value):
        #self.value = value
    def add(self):
        print("Add c")  

c1 = C()
c1.add()                      