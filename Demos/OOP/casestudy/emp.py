class Employee:
    def __init__(self,id,name,sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getId(self):
        return self.__id
    def setId(self,newid):
        self.__id = newid    

    def getName(self):
        return self.__name
    def setName(self,newname):
        self.__name = newname

    def getSal(self):
        return self.__sal
    def setSal(self,newsal):
        self.__sal = newsal
            

    def __str__(self):
        return f"ID = {self.__id}\t Name = {self.__name}\t Salary = {self.__sal} "
        
        