from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(N,x,y,MAP):
    q = deque()
    q.append([y,x])
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    cnt = 0
    while q:
        [y, x] = q.popleft()
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and MAP[ny][nx] == 1:
                return cnt
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and MAP[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny, nx])
def solution(N, bus_stop):
    answer = [[]]
    MAP = [[0]*N for _ in range(N)]
    for i in range(len(bus_stop)):
        MAP[bus_stop[i][0]-1][bus_stop[i][1]-1] = 1
    res = list([0] * N for _ in range(N))
    for y in range(N):
        for x in range(N):
            if MAP[y][x]:
                break
            res[y][x] = bfs(N,x,y,MAP)
    print(res)
    return answer

solution(3,[[1,2],[3,3]])