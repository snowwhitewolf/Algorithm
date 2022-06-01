for t in range(int(input())):
    a,b = map(int,input().split())
    res = 1
    for i in range(b):
        res *= a%10
        res = res%10
    if res == 0:
        print(10)
    else:
        print(res)