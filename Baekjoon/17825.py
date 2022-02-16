'''
말은 4개 이동횟수는 10번
값이 점점 커지므로 말 한개가 멀리 가는게 무조건 좋진 않음
값의 차이가 적다
총 경우의 수 4^10 작다
모든 경우의 수 찾음
'''
import itertools
from itertools import product


num = list(map(int, input().split()))
lst = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,
        26, 28, 30, 32, 34, 36, 38, 40],  # 반환점 없이 이동
    [10, 13, 16, 19, 25, 30, 35, 40],  # 10번에 갔을때
    [20, 22, 24, 25, 30, 35, 40],  # 20번에 갔을때
    [30, 28, 27, 26, 25, 30, 35, 40]  # 30번에 갔을때
]
visited = [
    [0]*len(lst[0]),
    [0]*len(lst[1]),
    [0]*len(lst[2]),
    [0]*len(lst[3]),
]
idx = [0, 0, 0, 0]  # 각 말의 위치
point = 0
result = 0
root = [0, 0, 0, 0]  # 이동하고 있는 경로
goal = [1, 1, 1, 1]  # 골인 유무

data = itertools.product([0, 1, 2, 3], repeat=10)
max_dis = [len(lst[0])-1]*4
for dice in data:
    point = 0
    for j in range(10):
        if goal[dice[j]]:  # 도착하지 않았을때
            if max_dis[j] < idx[j]+num[j]:  # 이번 이동으로 골인한다면
                goal[dice[j]] = 0
            elif visited[root[dice[j]]][idx[j]+num[j]] == 0:  # 중복이 아니면 이동
                visited[root[dice[j]]][idx[j]] = 0  # 원래 있던 자리 초기화
                idx[dice[j]] += num[j]  # 위치를 주사위 값만큼 이동
                visited[root[dice[j]]][idx[dice[j]]] = 1  # 지금 있는 자리 추가
                point += lst[root[dice[j]]][idx[dice[j]]]  # 점수 추가
                if lst[idx[dice[j]]] == 10:  # 10번에 위치
                    idx[dice[j]] = 0
                    root[dice[j]] = 1
                    max_dis[dice[j]] = len(lst[1]-1)
                elif lst[idx[dice[j]]] == 20:  # 20번에 위치
                    idx[dice[j]] = 0
                    root[dice[j]] = 2
                    max_dis[dice[j]] = len(lst[2]-1)
                elif lst[idx[dice[j]]] == 30:  # 30번에 위치
                    idx[dice[j]] = 0
                    root[dice[j]] = 3
                    max_dis[dice[j]] = len(lst[3]-1)
    result = max(result, point)

print(result)
