for t in range(int(input())):
    a,b,c = map(int,input().split())
    d = 0
    if a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a
    print('#{} {}'.format(t+1,d))