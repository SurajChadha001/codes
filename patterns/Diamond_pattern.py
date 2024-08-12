l = 5
for x in range(1, l  + 1):
    for y in range(1, l - x + 1):
        print(" ", end = "")
    for y in range(1, 2 * x):
        if y == 1 or y == 2 * x - 1:
            print("*",end="")
        else:
            print(" ", end="")
    print()
for x in range(l - 1, 0, -1):
    for y in range(1, l - x  + 1):
        print(" ", end ="")
    for y in range(1, 2 * x):
        if y == 1 or y == 2 * x - 1:
            print("*",end = "")
        else:
            print(" ", end="")
    print()
