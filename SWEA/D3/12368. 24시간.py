for t in range(int(input())):
    lst = list(map(int,input().split()))
    res = (lst[0] + lst[1])%24
    print('#{} {}'.format(t+1,res))