# 3. Create a class Shirt with members as sid,sname,typ(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook
class Shirt:
    def __init__(self,sid=1,sname ="AllonSoly",typ="Cotton",price=1500,size ="M/39"):
        self.sid = sid
        self.sname = sname 
        self.typ = typ
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Object is deleted")

    def showbook(self):
        print(f"ShirtID = {self.sid}\t ShirtName ={self.sname}\t TypeOfFabric ={self.typ}\t Price = {self.price}\t Size = {self.size} ") 

s1 = Shirt()
s1.showbook()

s1 = Shirt(101,"Mufti","Lenin",1500,"L")
s1.showbook
