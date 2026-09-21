class Add:
    def add_numbers(self):
        a = 10
        b = 20
        print("Addition of numbers:", a + b)

    def add_strings(self):
        s1 = "Hello "
        s2 = "Python"
        print("Addition of strings:", s1 + s2)

    def add_lists(self):
        list1 = [10, 20, 30]
        list2 = [40, 50, 60]
        print("Addition of lists:", list1 + list2)

class Time(Add):
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec
        
    def __add__(self, other):
        thr = self.hr + other.hr
        tmin = self.min + other.min
        tsec = self.sec + other.sec
        t = Time(thr,tmin,tsec)
        return t
    def __str__(self):
        return f"Hr = {self.hr} Min = {self.min} Sec = {self.sec}"
        


obj = Add()
obj.add_numbers()
obj.add_strings()
obj.add_lists()
t1 = Time(2,54,60)
t2 = Time(3,45,19)
print(t1+t2)

