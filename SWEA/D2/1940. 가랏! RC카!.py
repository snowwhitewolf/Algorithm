for t in range(int(input())):
    N = int(input())
    a = []
    v = 0
    result = 0
    for i in range(N):
        a.append(list(map(int, input().split())))
    for i in range(N):
        if a[i][0] == 1:
            v += a[i][1]
            result += v
        elif a[i][0] == 2:
            v -= a[i][1]
            if v <= 0:
                v=0
            else:
                result += v
        else:
            result += v
    print(f'#{t+1} {result}')