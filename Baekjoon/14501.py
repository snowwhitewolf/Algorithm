'''
n일 동안 최대로 수익을 내는 경우
1. 퇴사일까지 끝내지 못하는 상담은 할수 없음
2. n일부터 일을 하는 경우와 안하는 경우 중 큰값을 선택
'''

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
res = [0 for _ in range(n+1)] #받을수 있는 돈
pos = [0 for _ in range(n)] #일 가능 유무

for i in range(n):
    if i + lst[i][0] <= n:
        pos[i] = 1 #퇴사일을 넘어가서 불가능한 경우를 걸러냄

for i in range(n-1,-1,-1): #마지막 날부터 선택
    if pos[i]: #일을 할수 있으면
        res[i] = max(res[i+1], lst[i][1] + res[i + lst[i][0]])
        # 일을 안하는 경우(다음날까지 벌었던 돈) or 오늘 일을 하고 일을 마친 날까지의 번돈
    else:
        res[i] = res[i+1] # 일을 못하므로 번돈은 동일
print(res[0])
