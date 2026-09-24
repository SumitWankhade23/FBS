class Emp:
    def __init__(self,id,name,salary):
        self.eid = id            #public: Everyone in code
        self._nm = name          #protected: Available in class and subclasses
        self.__sal = salary      #privete: Only available inside the class

e1 = Emp(101,'ABC',50000)  

print(e1.eid)
print(e1._nm) #Not worked in python 
#print(e1.__sal) #raise error
print(e1._Emp__sal)
