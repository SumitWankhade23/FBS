#!. To make parameter optional 
#2. parameter -  default(Assigning the value to the parameter) 
#3. Assigning value -
#   if we pass the value to the default para, it takes a pass value
# If we don't pass the value to the dafault para, it takes default value 
#4. Flow from right to left
def emp(id, name=' ', sal=0, dep= 'Backoffice'):
    print('ID:',id)
    print('NAME:', name)
    print('SALARY:', sal)
    print('DEPT:', dep)

emp(101,'ABC',50000,'IT') 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
emp(102,'XYZ',10000)  
