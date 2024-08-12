lns = 5
cur_no = 2
for ln in range(1, lns+1):
    for position in range(1, ln + 1):
        while True:
            prime_no = True
            for ix in range(2, int(cur_no ** 0.5) + 1):
                if cur_no % ix == 0:
                    prime_no =  False
                    break
            if prime_no:
                break
            cur_no += 1

        print(cur_no, end=" ")
        cur_no += 1
    print()
