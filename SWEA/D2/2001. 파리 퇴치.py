for t in range(int(input())):
    M, N = map(int, input().split())
    lst = []
    for i in range(M):
        lst.append(list(map(int, input().split())))
    total = 0
    result = 0
    for y in range(M-N+1):
        for x in range(M-N+1):
            for i in range(N):
                for j in range(N):
                    total += lst[y+i][x+j]
            result = max(result, total)
            total = 0
    print(f'#{t+1} {result}')
