#Python Program to Find the Second Largest Number in a List Using Bubble Sort
def secLarg_num(data):
    max = 0
    s_max = 0
    for ind in range(1, len(data)):
        if max < data[ind]:
            s_max = max
            max = data[ind]
        elif(s_max < data[ind]):
            s_max = data[ind]
    return s_max
        
data = [10,20,30,99,45,78,98,40,50,60]
result = secLarg_num(data)
print(f"Second Larges Element: {result}")    
