for t in range(int(input())):
    N, M = map(int, input().split())
    b = N-M
    a = M-b
    print('#{} {} {}'.format(t+1, a, b))
