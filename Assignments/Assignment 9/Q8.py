#8. Write a program to check whether a number is prime or not using recursion.
def check_num_prime(n,d):
    if( n < 2):
        return False
    elif( d == n):
        return True
    elif n % d == 0:
        return False
    return check_num_prime(n,d+1)
    

n = int(input("Enter number: "))
result = check_num_prime(n,2)
if result:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")    

