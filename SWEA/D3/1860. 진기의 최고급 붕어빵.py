for t in range(int(input())):
    n,m,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    res = 'Possible'
    order = 0
    for i in lst:
        if (i//m)*k-order < 1 or i < m:
            res = 'Impossible'
            break
        else:
            order += 1
    print('#{} {}'.format(t+1,res))
