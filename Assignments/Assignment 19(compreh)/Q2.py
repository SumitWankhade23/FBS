# 2. Find all of the numbers from 1–1000 that have a 6 in them
nu = [i for i in range(1,1001) if '6' in str(i)]
print(nu)


#From second method without converting the int into string
def has_six(n):
    while n > 0:
        if n % 10 == 6:     
            return True
        n //= 10           
    return False

nu = [i for i in range(1, 1001) if has_six(i)]
print(nu)

