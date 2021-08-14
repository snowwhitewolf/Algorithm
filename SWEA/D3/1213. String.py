for _ in range(10):
    t = int(input())
    short = str(input())
    long = str(input())
    cnt = 0
    for i in range(len(long)-len(short)+1):
        if long[i:i+len(short)] == short:
            cnt += 1
    print(f'#{t} {cnt}')