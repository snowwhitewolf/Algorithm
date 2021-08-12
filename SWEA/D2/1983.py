for t in range(int(input())):
    N, K = map(int,input().split())
    lst =[list(map(int,input().split())) for i in range(N)]
    result=[]
    for i in ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']:
        for j in range(N//10): 
            result.append(i)

    total = []
    for i in range(N):
        total.append(lst[i][0]*0.35 + lst[i][1]*0.45 + lst[i][2]*0.2)
    rank = sorted(total, reverse=True)
    for i in range(N):
            if total[K-1] == rank[i]:
                print(f'#{t+1} {result[i]}')