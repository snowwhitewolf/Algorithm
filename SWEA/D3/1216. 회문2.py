def garo(lst, k):
    for y in range(100):
        for x in range(101 - k):
            if lst[y][x:x+k] == lst[y][x:x+k][::-1]:
                return 1
    return 0


def sero(lst, k):
    for y in range(101-k):
        for x in range(100):
            A = ''
            for z in range(k):
                A += lst[y+z][x]
            if A == A[::-1]:
                return 1


for tc in range(10):
    t = int(input())
    lst = []
    cnt = 0
    for l in range(100):
        lst.append(list(map(str, input().strip())))
    k = 100
    while cnt == 0:
        if garo(lst, k) or sero(lst, k):
            cnt = k
            break
        k -= 1

    print(f'#{t} {cnt}')
