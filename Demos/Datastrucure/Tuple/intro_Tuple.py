#1. ( )
tu = (10,20,30)
tu1 = (10)
tu2 = (10,)
print(type(tu1))
print(type(tu2))

#2. Heterogeneous
tu3 = (10,'abc',20,30)
print(tu3)

#3. Orderd collection of data

#4. Immutable
#tu3[0] = 7  

#5. Duplication is allowed

#size cheack
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))



