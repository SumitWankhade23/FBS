#abstract method 
#1. Need to impliment compulsory in subclasses
#2. No body only defination

from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def stop():
        pass
#v1 = Vehical() #Can't instantiate  

class Bike(Vehical):
    def start(self):
        print("Start method")
    def stop(self):
        print("Stop method")  

b1 = Bike()
b1.start()
b1.stop()        
