l = 5
for x in range(l, l + 1):
    print(' ' * (l-x) + '*' * (2 * x - 1))
for y in range(l - 1, 0, -1):
    print(' ' * (l - y) + '*' * (2 * y - 1))
