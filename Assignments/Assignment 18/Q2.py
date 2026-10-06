# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
#     a. Constructor
#     b. Destructor
#     c. Overload +,- operator
class Distance:
    def __init__(self, km=0, m=0, cm=0):
        total_cm = km * 100000 + m * 100 + cm
        self.km = total_cm // 100000
        remaining = total_cm % 100000
        self.m = remaining // 100
        self.cm = remaining % 100

    def __del__(self):
        print(f"Destructor called for {self}")

    def to_cm(self):
        return self.km * 100000 + self.m * 100 + self.cm

    def __add__(self, other):
        return Distance(0, 0, self.to_cm() + other.to_cm())

    def __sub__(self, other):
        result = self.to_cm() - other.to_cm()
        if result < 0:
            raise ValueError("Result of subtraction cannot be negative")
        return Distance(0, 0, result)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


d0 = Distance()
d1 = Distance(5, 800, 60)
d2 = Distance(2, 300, 70)

print("d1 =", d1)
print("d2 =", d2)

d3 = d1 + d2
d4 = d1 - d2
print("d1 + d2 =", d3)
print("d1 - d2 =", d4)

