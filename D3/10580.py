for t in range(int(input())):
    N = int(input())
    a = []
    result = 0
    for i in range(N):
        a.append(list(map(int, input().split())))

    for i in range(N-1):
        for j in range(i,N):
            if a[i][0] > a[j][0] and a[i][1] < a[j][1]:
                result +=1
            elif a[i][0] < a[j][0] and a[i][1] > a[j][1]:
                result +=1
    print(f'#{t+1} {result}')

