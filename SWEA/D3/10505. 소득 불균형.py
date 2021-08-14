for t in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    avg = sum(lst)/N
    cnt = 0
    for i in range(N):
        if lst[i] <= avg:
            cnt += 1
    print(f'#{t+1} {cnt}')