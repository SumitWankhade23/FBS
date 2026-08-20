#1.To neglect the positional parameter
#2. Assign value to parameter in function call
#3. Paramter name in function defination and function call should be same
#4. Flow from right to left
def emp(id, name, sal, dep):
    print('ID:',id)
    print('NAME:', name)
    print('SALARY:', sal)
    print('DEPT:', dep)

emp(name='ABC', sal = 50000, dep='IT',id = 101 ) 
print("===============================================") 
emp(102,'XYZ',dep= 'IT',sal= 10000)  
