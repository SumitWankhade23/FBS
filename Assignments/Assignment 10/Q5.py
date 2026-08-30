# #5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.
def check_ele(data,num):
    count = 0
    i = 0
    while( i < len(data)):
        
        if num == data[i]:
            count += 1
        i += 1
    if( count > 0):
        print(f'{num} is presnt')
        print(f"Occurance of number = {count} time")       
    else:
        print(f"Number is not present in list")

data = [10,20,30,20,20,20,40,50,60,70]
print(data)
num = int(input("Enter the number to be checked: ")) 
check_ele(data,num)       
            
