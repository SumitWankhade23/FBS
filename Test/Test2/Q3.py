# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

l = 50
b = 40
r = 20
pi = 3.14
cost_wire = 35

half_circle = pi * r
Two_length = l + l
one_breath = b

PF = half_circle + Two_length + one_breath
print("Perimeter of the filed = ",PF)

Totalwire_length = PF * 5
cost = Totalwire_length * cost_wire
print("cost of fencing the field = ",cost,"Rs")


