T = int(input())

for t in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    if N <= M:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    else:
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))

    total = 0
    result = 0
    cnt = 0

    while abs(M-N) >= cnt:
        for i in range(min(M, N)):
            total += a[i]*b[i+cnt]
        result = max(total, result)
        total = 0
        cnt += 1

    print(f'#{t} {result}')
