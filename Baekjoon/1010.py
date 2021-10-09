import math
for t in range(int(input())):
    N,M = map(int,input().split())
    res = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))
    print(res)