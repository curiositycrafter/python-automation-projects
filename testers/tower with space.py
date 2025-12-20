n=8
for row in range(n):
    for col in range(n):
        if col>=n-row-1 and  (col-row-1)%2==0 and col<:
            print('*',end='')
        else:
            print(' ',end='')
    print()