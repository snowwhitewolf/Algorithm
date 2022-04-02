from itertools import combinations


def score(lst_1, lst_2):
    team1 = 0
    team2 = 0
    for i in lst_1:
        for j in lst_1:
            team1 += lst[i-1][j-1]
    for i in lst_2:
        for j in lst_2:
            team2 += lst[i-1][j-1]
    return abs(team1-team2)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
total = list(range(1, N+1))
res = 100000000
team = list(combinations(total, N//2))

for q in range(len(team)):
    team_1 = []
    for w in team[q]:
        team_1.append(w)
    team_2 = [k for k in total if k not in team_1]
    res = min(res, score(team_1, team_2))
print(res)
