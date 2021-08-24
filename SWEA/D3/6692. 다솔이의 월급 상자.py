for t in range(int(input())):
    n = int(input())
    lst = []
    result = 0
    for i in range(n):
        a,b = map(float,input().split())
        result += a*b
    print('#{} {}'.format(t+1,result))