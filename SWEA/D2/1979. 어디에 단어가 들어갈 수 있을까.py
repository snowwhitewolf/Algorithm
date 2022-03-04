for t in range(int(input())):
    N, K = map(int, input().split())
    box = [[0 for _ in range(N+2)] for _ in range(N+2)]

    for i in range(1, N+1):
        box[i] = list(map(int, input().split()))
        box[i].insert(0, 0)
        box[i].append(0)

    result = 0
    x = 0
    y = 0
    total = []
    test = [1 for _ in range(K)]
    test.insert(0, 0)
    test.append(0)
    for i in range(1, N+1):
        for j in range(N-K+1):
            if box[i][j:j + K+2] == test:
                result += 1
    up = 0
    for j in range(1, N+1):
        up = 0
        while up != N-K+1:
            for i in range(up, up+K+2):
                total.append(box[i][j])
            if total == test:
                result += 1
            up += 1
            total = []
    print(f'#{t+1} {result}')
