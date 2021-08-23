for t in range(int(input())):
    N = int(input())
    lst = []
    num = ''
    while len(num) != N:
       num += ''.join(map(str,input().split()))
    i = 0
    while True:
        if str(i) in num:
            i += 1
        else:
            break
    print('#{} {}'.format(t + 1, i))