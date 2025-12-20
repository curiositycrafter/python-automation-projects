n=4
for i in range(n):
    for j in range(8):
        if i+j>=8//2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()