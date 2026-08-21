li = [10,20,30,99,45,78,45,98,40,50,60]

max = li[0]
for ind in range(0, len(li)):
    if max < li[ind]:
        max = li[ind]
print("Maximum: ",max)    

#                    MEMORY / OBJECTS

# Variables                    List Object
# ┌─────────────┐              ┌──────────────────────────────────────┐
# │ data ───────┼─────────────►│ 10 20 30 99 45 78 45 78 98 40 50 60  │
# │             │              └──────────────────────────────────────┘
# │ maximum=99  │
# │ smax=98     │
# │ i=6         │
# └─────────────┘
    
    