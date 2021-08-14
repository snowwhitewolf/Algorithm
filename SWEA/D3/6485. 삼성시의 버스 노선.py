for t in range(int(input())):
    N = int(input())
    line = []
    bustop = []
    for i in range(N):
        line.append(list(map(int,input().split())))
    P = int(input())
    result = [0 for _ in range(P)]
    for i in range(P):
        bustop.append(int(input()))
    for i in range(N):
        for j in range(P):
            if line[i][0] <= bustop[j] <= line[i][1]:
                result[j] += 1
    print('#{}'.format(t+1),end=' ')
    print(*result)