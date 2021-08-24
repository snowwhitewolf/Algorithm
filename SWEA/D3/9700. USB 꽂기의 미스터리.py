for t in range(int(input())):
    p,q=map(float,input().split())
    s1 = (1-p)*q
    s2= p*(1-q)*q
    if s1 > s2:
        print('#{} NO'.format(t+1))
    else:
        print('#{} YES'.format(t+1))