for t in range(int(input())):
    N,Q = map(int,input().split())
    lst = [[0,0]]
    for i in range(Q):
        lst.append(list(map(int,input().split())))
    result = [0 for _ in range(N+1)]
    for i in range(1,Q+1):
        for j in range(lst[i][0],lst[i][1]+1):
            result[j] = i
    print(f'#{t+1}',end=' ')
    print(*result[1:])
