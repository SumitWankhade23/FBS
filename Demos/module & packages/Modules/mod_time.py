import time
print(time.time())
# for i in range(1,10):
#     time.sleep(1)
#     print(i)
print(time.ctime())
t = time.localtime() 
print(t) 
print(t.tm_year)
print(t.tm_mon)  