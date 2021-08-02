T = int(input())

for t in range(1,T+1):
    NK = list(map(int, input().split()))
    N = NK[0]
    k = NK[1]
    n_list = list(map(int, input().split()))
    total = list(range(1,N+1))
    for i in range(len(n_list)):
        if n_list[i] in total:
            total.remove(n_list[i])
    print(f'#{t}', end = ' ')
    print(*total)
