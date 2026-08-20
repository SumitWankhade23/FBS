for i in range(1,6):
    for j in range(0,5-i):
        print("  ", end="")
    for j in range(i, i*2):
        print(j, end=" ")
    for j in range(i*2 - 2, i - 1, -1):
        print(j, end=" ")

    print()