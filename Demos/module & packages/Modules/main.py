#1. import demo1
# demo1.add(12,2)
# print(demo1.pname)

#2. from modulname import member
# from demo1 import add
# add(12,5)

#3. from module name import member
# from demo1 import add,pname
# add(12,5)
# print(pname)

#4. from modulename import all(*)
# from demo1 import *
# add(12,4)
# sub(12,3)
# print(pname)

#5. Alicename()
import demo1 as d
d.add(12,8)
d.sub(12,5)
print(d.pname)

