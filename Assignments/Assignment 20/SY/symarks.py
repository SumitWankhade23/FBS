class SYmarks:
    def __init__(self,computer_total=0,maths_total=0, electronics_total=0):
        self.computer_total = computer_total
        self.maths = maths_total
        self.electronics = electronics_total

    def __str__(self):
        return (f"ComputerTotal ={self.computer_total}, MathsTotal = {self.maths}"
               f"Electronics = {self.electronics}")
