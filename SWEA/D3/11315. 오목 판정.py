def func(N, a):
    for y in range(N):
        for x in range(N-4):
            if a[y][x:x+5] == ['o', 'o', 'o', 'o', 'o']:
                return 1

    for x in range(N):
        up = 0
        while up <= N - 5:
            aa = []
            for y in range(up, 5 + up):
                aa.append(a[y][x])
            if aa == ['o', 'o', 'o', 'o', 'o']:
                return 1
            up += 1

    for y in range(N - 4):
        for x in range(N - 4):
            aa = []
            up = 0
            for k in range(5):
                aa.append(a[y + up][x + up])
                up += 1
            if aa == ['o', 'o', 'o', 'o', 'o']:
                return 1

    for y in range(N - 4):
        for x in range(N-1,3,-1):
            aa = []
            up = 0
            for k in range(5):
                aa.append(a[y + up][x - up])
                up += 1
            if aa == ['o', 'o', 'o', 'o', 'o']:
                return 1
    return 0


for t in range(int(input())):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(str, input().strip())))
    if func(N, lst) == 1:
        print('#{} YES'.format(t+1))
    else:
        print('#{} NO'.format(t+1))