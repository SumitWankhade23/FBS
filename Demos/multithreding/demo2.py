from time import sleep
from threading import Thread
class Demo(Thread):
    def run(self):
        for i in range(5):
            print("Pizza","🍕🍕🍕")
            sleep(1)
class Demo1(Thread):
    def run(self):
        for i in range(2):
            print("Burger","🍔🍔🍔") 
            sleep(2)
d1 = Demo()
d2 = Demo1()
# d1.run()
# d2.run()
d1.start()
d2.start()
