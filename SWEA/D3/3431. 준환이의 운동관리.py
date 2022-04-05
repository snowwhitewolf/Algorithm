for t in range(int(input())):
    L, U, X = map(int, input().split())
    a = 0
    if X > U:
        a = -1
    elif L > X:
        a = L - X
    print(f'#{t+1} {a}')
