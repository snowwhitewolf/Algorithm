for t in range(int(input())):
    a = ['']+list(input().strip())
    h = int(input())
    lst = list(map(int,input().split()))
    for i in lst:
        if i == 0:
            a[0] += '-'
        else:
            a[i] += '-'
    print('#{}'.format(t+1),end=' ')
    print(''.join(a))