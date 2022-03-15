from collections import deque

def bfs(y,x):
    global n
    visited = list([0] * M for _ in range(N))
    q = deque()
    family = []
    q.append([y,x])
    visited[y][x] = 1
    family.append([y, x])
    cnt = 1

    while q:
        [nowy, nowx] = q.popleft()
        for d in range(4):
            ny = nowy + dy[d]
            nx = nowx + dx[d]
            if 0<= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and MAP[ny][nx] == 0:
                q.append([ny,nx])
                family.append([ny,nx])
                visited[ny][nx] = 1
                cnt += 1
    for i in range(len(family)):
        number[family[i][0]][family[i][1]] = n
    cnt_lst.append(cnt%10)
    n += 1
    return

N, M = map(int, input().split())
MAP = [list(map(int,input().rstrip())) for _ in range(N)]
res = list([0]*M for _ in range(N))
n = 1
number = list([0]*M for _ in range(N))
dy = [1,-1,0,0]
dx = [0,0,1,-1]
cnt_lst = [0]


for y in range(N):
    for x in range(M):
        if MAP[y][x] == 0 and number[y][x] == 0:
            bfs(y,x)

for y in range(N):
    for x in range(M):
        if MAP[y][x]:
            num = []
            total = 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < M and MAP[ny][nx] == 0 and number[ny][nx] not in num:
                    num.append(number[ny][nx])
                    total += cnt_lst[number[ny][nx]]
            res[y][x] = total%10
for y in range(N):
    print(res[y])
