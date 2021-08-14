import math
for t in range(int(input())):

    cnt = 0
    a, b = map(int,input().split())
    lst = list(range(a,b+1))
    def func(w):
        if len(w) == 1:
            return 1
        for i in range(len(w) // 2):
            if w[i] != w[len(w)-i]:
                return 0
        return 1
    for i in range(len(lst)):
        if func(str(lst[i])) and type(int(math.sqrt(lst[i]))) == type(1) and func(str(int(math.sqrt(lst[i])))):
            cnt +=1
    print(f'#{t+1} {cnt}')