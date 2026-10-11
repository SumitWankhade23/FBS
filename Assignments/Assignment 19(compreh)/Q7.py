# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.
#-------------------------------------------------------------------
li = [n for n in range(1, 1001) if [d for d in range(2, 10) if n % d == 0]]
print(li)
print("Count:", len(li))
