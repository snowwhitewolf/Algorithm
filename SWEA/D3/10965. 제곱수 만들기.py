num = [1]*int((10**7)**0.5)
sosu = []
for i in range(2,int((10**7)**0.5)+1):
    if num[i-1]:
        sosu.append(i)
        for j in range(i-1, int((10**7)**0.5), i):
            num[j] = 0
prin = []
for t in range(int(input())):
    a = int(input())
    b=1
    for s in sosu:
        if s > a:
            break
        cnt = 0
        while a % s == 0:
            a = a //s
            cnt += 1
        if cnt % 2 == 1:
            b *= s
    if a > 1:
        b *= a
    prin.append('#{} {}'.format(t+1, b))
for p in prin:
    print(p)