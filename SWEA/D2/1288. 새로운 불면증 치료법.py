for t in range(int(input())):
    N = int(input())
    num = list(range(10))
    total = []
    n = N
    while len(total) < 10:
        for i in range(len(str(n))):
            total.append(int(str(n)[i]))
        total = sorted(list(set(total)))
        n += N
    print('#{} {}'.format(t+1,n-N))
