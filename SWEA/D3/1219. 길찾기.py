for _ in range(10):
    lst = list([0 for _ in range(101)] for _ in range(101))
    t, n = map(int,input().split())
    go = list(map(int,input().split()))
    for i in range(0,2*n,2):
        lst[go[i]][go[i+1]] = 1
    gg = 0
    visited = list(0 for _ in range(101))
    def dfs(now):
        for next in range(1, 101):
            if lst[now][next] == 1 and visited[next] == 0:
                if next == 99:
                    global gg
                    gg = 1
                    break
                visited[next] = 1
                dfs(next)
        return

    dfs(0)
    print('#{} {}'.format(t,gg))