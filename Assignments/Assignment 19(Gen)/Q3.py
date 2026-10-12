# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError("step must not be zero")

    current = start
    if step > 0:
        while current < stop:       
            yield current
            current += step
    else:
        while current > stop:       
            yield current
            current += step         



print(list(my_range(5)))             
print(list(my_range(2, 8)))          
print(list(my_range(1, 10, 3)))      
print(list(my_range(10, 0, -2)))     

for n in my_range(1, 6):
    print(n, end=" ")                