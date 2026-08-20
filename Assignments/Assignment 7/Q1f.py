for i in range(1,6):
    for j in range(i,6):
        if i == 1:
            print(j, end="  ")
        elif j == i:
            print(i, end="  ")
        elif j == 5:
            print(j, end="  ")
        else:
            print(" ", end="  ")
    print()