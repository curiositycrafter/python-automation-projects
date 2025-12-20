
for i in range(4):
    for j in range(8):
        if i+j>=8//2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()