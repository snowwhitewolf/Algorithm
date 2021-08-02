T = int(input())

for t in range(1,T+1):
    N = int(input())
    result = [[0]*N for i in range(N)]
    d =1
    up = 0

    for e in range(N):
        #오른쪽으로 이동
        for i in range(0+up,N-up):
            result[up][i] = d
            d += 1
            if d >= N*N:
                break
    
        #아래로 이동
        for i in range(1+up, N-up):
            result[i][N-1-up] = d
            d += 1
            if d >= N*N:
                break

        #왼쪽으로 이동
        for i in range(N-2-up,-1+up,-1):
            result[N-1-up][i] = d
            d += 1
            if d >= N*N:
                break
        
        # 위쪽으로 이동
        for i in range(N-2-up,0+up,-1):
            result[i][0+up] = d
            d += 1
            if d >= N*N:
                break
        up += 1


    print(f'#{t}')
    for i in range(N):
        print(*result[i])
