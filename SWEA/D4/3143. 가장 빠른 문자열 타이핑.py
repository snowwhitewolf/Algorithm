for t in range(int(input())):
    A, B = map(str,input().split())
    l = []
    s = []
    for i in A:
        l.append(i)
    for i in B:
        s.append(i)
    cnt = 0
    i=0
    while len(l) != 0:
        if l[i:i + len(s)] == s:
            cnt += 1
            l = l[i + len(s):]
            i=0
        else:
            l = l[1:]
            cnt += 1

    print(f'#{t+1} {cnt}')