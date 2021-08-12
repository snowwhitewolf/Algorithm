for t in range(int(input())):
    m = list(map(int,input().strip()))
    x = [0 for _ in range(len(m))]
    cnt = 0
    for i in range(len(m)):
        if m[i] != x[i]:
            if m[i] == 1:
                for j in range(len(m)-i):
                    x[i+j] = 1
                cnt += 1
            elif m[i] == 0:
                for j in range(len(m)-i):
                    x[i+j] = 0
                cnt += 1
            if m == x:
                break
    print(f'#{t+1} {cnt}')