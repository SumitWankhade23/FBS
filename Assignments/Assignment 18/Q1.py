# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
    # a. Constructor
    # b. Destructor
    # c. Overload +,- operator
class Complex_Number:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print(f"Destructor called for {self}")

    def __add__(self,other):
        return Complex_Number(self.real + other.real, self.imag + other.imag)  

    def __sub__(self, other):
        return Complex_Number(self.real - other.real, self.imag + other.imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        return f"{self.real} - {self.imag}i"

c1 = Complex_Number()
c2 = Complex_Number(3,4)
c3 = Complex_Number(6,7)

print("c1 = ",c1)
print("c2 = ",c2)
print("c3 =",c3)

c4 = c2 + c3
c5 = c2 - c3

print("c2 + c3 =",c4)
print("c2 - c3 =",c5)

