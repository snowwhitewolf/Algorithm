for t in range(int(input())):
    N = int(input())
    lst = []
    room = [0]*400
    for i in range(N):
        lst.append(list(map(int,input().split())))
        for j in range(2):
            if lst[i][j]%2 == 0:
                lst[i][j] = lst[i][j]-1
    for i in range(N):
        for j in range(min(lst[i]), max(lst[i])+1):
            room[j] += 1
    print(f'#{t+1} {max(room)}')