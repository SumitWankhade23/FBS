#1. To pass multiple values with meaning to function 
#2. Mention 2 asterisk symbols before  paramter name in function defination
#3. Passed data stored in dictionary format 
#4. use for loop on dict.items() to get values and kyes

def emp(**data):
    print(type(data))
    for key, val in data.items():
        print(key,':',val)
    

emp(id= 101, age = 35, add= 'Pune', sal = 50000, dept = 'IT')        