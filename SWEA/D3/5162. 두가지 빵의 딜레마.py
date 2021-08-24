for t in range(int(input())):
    a,b,c = map(int,input().split())
    d = min(a,b)
    print('#{} {}'.format(t+1,c//d))