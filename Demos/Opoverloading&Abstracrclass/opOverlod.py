class Time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec 
    def __str__(self):
        return f"Hr = {self.hr} Min = {self.min} Sec = {self.sec}"
    def __add__(self, other):
        thr = self.hr + other.hr
        tmin = self.min + other.min
        tsec = self.sec + other.sec
        t = Time(thr,tmin,tsec) 
        return t

t1 = Time(2,60,60)
t2 = Time(4,12,10)
#t1.display()
print(t1)
print(t2)
print(t1+t2)