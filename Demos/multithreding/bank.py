from threading import Thread,Lock
from time import sleep
class Bank:
    balance = 1000                                           #Hardcoded value 
    l1=Lock()
    def withdrawl(self,amount):
        Bank.l1.acquire()                                    #Lock start here whole program is lock 
        if  Bank.balance >= amount:
            print(f"Processing withdrawl of {amount}")
            old_balance = Bank.balance
            sleep(1)
            Bank.balance = old_balance - amount
            print(f"Withdrawl of {amount} sucessful")  
        else:
            print(f"Insufficint balance for {amount}")     
        Bank.l1.release()                                    #Lock is open
b1 = Bank()
t1 = Thread(target=b1.withdrawl,args=(700,))
t2 = Thread(target=b1.withdrawl,args=(500,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Final balance", Bank.balance)