for i in range(1, 10, 2):

    
    for j in range(1, 10 - i, 2):
        print(" ", end=" ")

    
    for j in range(i):
        print(chr(65 + j), end=" ")

    print()