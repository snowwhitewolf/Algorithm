for t in range(1, int(input())+1):
    n = int(input())
    before = list(map(int, input().split()))
    m = int(input())
    change = []
    now = [0]*n
    q = 0
    for _ in range(m):
        a = list(map(int, input().split()))
        change.append(a)

    def func(n, m):
        global q
        nowin = 0
        for i in range(n):
            a = before[i]
            cnt = 0
            for j in range(m):
                if a in change[j]:
                    for k in range(2):
                        if change[j][k] != a and change[j][k] not in before[:i]:
                            cnt += 1
            if cnt and now[i+cnt] == 0:
                now[i+cnt] = a
            else:
                while True:
                    if now[nowin] == 0:
                        now[nowin] = a
                        break
                    else:
                        nowin += 1
        return
    func(n, m)
    if 0 in now:
        if q == 0:
            print("?")
    else:
        print(*now)
