n=8
for i in range(n):
    for j in range(n):
        if j>=n-i-1 or j-n-i-1%2==0:
            print('*',end='')
        else:
            print(' ',end='')
    print()