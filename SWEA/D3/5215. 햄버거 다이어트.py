for t in range(int(input())):
    N, L = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = arr[0][0]

    for i in range(1 << N):
        cal = 0
        point = 0
        for j in range(N):
            if i & (1 << j):
                cal += arr[j][1]
                point += arr[j][0]
        if (cal <= L) & (point > result):
            result = point
    print('#{} {}'.format(t+1,result))