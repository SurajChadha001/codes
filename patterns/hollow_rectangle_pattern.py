p = 6
q = 6
for x in range(p):
    if x==0 or x==p-1:
        print('*'*q)
    else:
        print('*'+' ' * (q-2) + '*' )
