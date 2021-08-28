from collections import deque
for t in range(10):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(100)]
    for y in range(100):
        for x in range(100):
            if maze[y][x] == 2:
                sty,stx = y, x
            elif maze[y][x] == 3:
                resy,resx = y, x
    dx = [-1,0,1,0]
    dy = [0, 1, 0, -1]
    def bfs(sty1,stx1):
        visited = [[0] * 100 for _ in range(100)]
        queue = deque()
        queue.append((sty1, stx1))
        while queue:
            y,x = queue.popleft()
            if x == resx and y == resy:
                return 1
            for i in range(4):
                nextx = x + dx[i]
                nexty = y + dy[i]
                if maze[nexty][nextx] == 0 and visited[nexty][nextx]==0:
                    queue.append((nexty, nextx))
                    visited[nexty][nextx] = 1
                if maze[nexty][nextx] == 3:
                    return 1
        return 0
    print('#{} {}'.format(tc,bfs(sty,stx)))