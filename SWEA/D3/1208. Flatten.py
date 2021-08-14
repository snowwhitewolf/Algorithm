for t in range(10):
    d = int(input())
    b = list(map(int,input().split()))
    while d != 0:
        b.sort()
        b[0] += 1
        b[-1] -= 1
        d -= 1
    print(f'#{t+1} {max(b)-min(b)}')