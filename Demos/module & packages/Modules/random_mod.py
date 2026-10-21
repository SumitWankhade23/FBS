import random
print(int(random.random()*10000))
print(random.randint(100,999))
print(random.randrange(1000,10000))#
li = ["Sumit","MSD","Rohit","Sachin"]
print(random.choice(li))
print(li)
random.shuffle(li)
print(li)