rows = 5
outer_spaces = rows - 1
inner_spaces = 1

for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print(' ' * outer_spaces + '*' * (2*i-1))
        outer_spaces -= 1
    else:
        print(' ' * outer_spaces + '*' + ' ' * inner_spaces + '*')
        outer_spaces -= 1
        inner_spaces += 2

        
