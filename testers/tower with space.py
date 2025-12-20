n=8
for i in range(n):
    for j in range(8):
        if j>n-i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()