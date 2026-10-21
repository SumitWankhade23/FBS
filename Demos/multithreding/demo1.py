from time import sleep
from threading import Thread
def fun1():
    for i in range(5):
        print("Virat")
        sleep(1)
def fun2():
    for i in range(2):
        print("Sachin")        
        sleep(1)
# fun1()
# fun2() 
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()# This will start the processes 
t2.start()
t1.join()#It helps to create thread wait
t2.join()# This will control the main thread after complition of all the thread will execute 
print("I am in main thread ")      