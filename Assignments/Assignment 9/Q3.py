#3. Write a program to reverse a given number using recursive function.
def rev(n,r):
    if( n == 0):
        return r
    else:
        r = r * 10 + (n%10)
        return rev(n//10,r)

n = int(input("Enter number: "))
r = 0
print("Reverse of number: ",rev(n,r))