for t in range(int(input())):
    a = input()
    b = a[::-1]
    c = ''
    for i in b:
        if i == 'b':
            c += 'd'
        elif i == 'd':
            c += 'b'
        elif i == 'q':
            c += 'p'
        elif i == 'p':
            c += 'q'
    print('#{} {}'.format(t+1,c))