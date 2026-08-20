def armstrong_num(num):
    n = num 
    count = 0
    rev = 0
    while( n > 0):
        count += 1
        n //= 10
    n = num
    while( n > 0):
        rev = rev + (n%10)** count
        n //= 10
    if(num == rev):
        return True
    else:
        return False

num = [153,584,371,254,658,475]
res = list(map(armstrong_num,num))

print(res)

