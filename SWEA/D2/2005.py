for t in range(int(input())):
    N=int(input())
    result = []
    for i in range(1,N+1):
        result.append([0]*i)
    for i in range(0,N):
        result[i][0] = 1
        result[i][-1] =1
        for j in range(1,i):
            result[i][j] += result[i-1][j-1] + result[i-1][j]

    print(f'#{t+1}')
    for i in range(N):
        print(*result[i])