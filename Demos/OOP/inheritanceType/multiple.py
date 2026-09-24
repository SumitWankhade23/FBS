class Mech:
    def display(self):
        print("I am mechnical")
class Elect:
    def display(self):
        print("i am Elect telecom") 
class Mechatronix(Mech,Elect):
    def abc(self):
        print("I am in mechtronix")  
m = Mechatronix()
m.display()                     