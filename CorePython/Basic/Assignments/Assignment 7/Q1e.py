for i in range(1, 6):
    for j in range(0,6- i):
        print("  ", end="")

    
    for j in range(1, i + 1):

        if j == 1 or j == i or i == 5:
            print(j, end="   ")
        else:
            print(" ", end="   ")

    print()