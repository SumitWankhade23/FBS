# 4. Write a program to print pattern
#         10101
#         01010
#         10101
#         01010
#         10101
for i in range(1,6):
    for j in range(1,6):
        if (j+i)% 2 == 0:
            print("1",end=" ")
        else:
            print("0",end=" ") 
    print()           