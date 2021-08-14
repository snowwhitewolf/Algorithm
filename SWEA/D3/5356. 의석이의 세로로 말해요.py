for t in range(int(input())):
    lst = ['' for _ in range(5)]
    maxx = 0
    result = ''
    for i in range(5):
        lst[i] = str(input())
        if len(lst[i]) > maxx:
            maxx = len(lst[i])
    for i in range(maxx):
        for k in range(5):
            if len(lst[k]) >= i+1:
                result += lst[k][i]
    print('#{} {}'.format(t+1,result))