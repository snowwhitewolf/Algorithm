T = int(input())

for t in range(1,T+1):
    N = int(input())
    num = [range(10)]
    total = []
    result =0
    n = N
    while num != list(set(total)).sort():
        for i in range(len(str(n))):
            total.append(int(str(n)[i]))
        n += N
    result = n//N
    print(result)
