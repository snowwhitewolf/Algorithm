for t in range(int(input())):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    lst2 = list([0 for _ in range(N)] for _ in range(N))
    lst3 = list([0 for _ in range(N)] for _ in range(N))
    lst4 = list([0 for _ in range(N)] for _ in range(N))
    result = []
    for i in range(N):
        for j in range(N):
            lst2[j][i] = lst[N-i-1][j]

    for i in range(N):
        for j in range(N):
            lst3[j][i] = lst2[N-i-1][j]

    for i in range(N):
        for j in range(N):
            lst4[j][i] = lst3[N-i-1][j]
    print(f'#{t+1}')
    for i in range(N):
        for j in range(N):
            print(lst2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(lst3[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(lst4[i][j], end='')
        print()
