def func(lst):
    for y in range(4):
        cntx = 0
        cnto = 0
        for x in range(4):
            if lst[y][x] == 'X' or lst[y][x] == 'T':
                cntx += 1
            if lst[y][x] == 'O' or lst[y][x] == 'T':
                cnto += 1
        if cntx == 4:
            return 'x'
        elif cnto == 4:
            return 'o'
    for x in range(4):
        cntx = 0
        cnto = 0
        for y in range(4):
            if lst[y][x] == 'X' or lst[y][x] == 'T':
                cntx += 1
            if lst[y][x] == 'O' or lst[y][x] == 'T':
                cnto += 1
        if cntx == 4:
            return 'x'
        elif cnto == 4:
            return 'o'
    cntx = 0
    cnto = 0
    for i in range(4):
        if lst[i][i] == 'X' or lst[i][i] == 'T':
                cntx += 1
        if lst[i][i] == 'O' or lst[i][i] == 'T':
            cnto += 1
    if cntx == 4:
            return 'x'
    elif cnto == 4:
        return 'o'
    cntx = 0
    cnto = 0
    for i in range(4):
        if lst[i][3-i] == 'X' or lst[i][3-i] == 'T':
                cntx += 1
        if lst[i][3-i] == 'O' or lst[i][3-i] == 'T':
            cnto += 1
    if cntx == 4:
        return 'x'
    elif cnto == 4:
        return 'o'
    for y in range(4):
        for x in range(4):
            if lst[y][x] == '.':
                return 'n'
    return 'd'
for t in range(int(input())):
    lst = [list(map(str,input().strip())) for _ in range(4)]
    b = input()
    if func(lst) == 'x':
        print('#{} X won'.format(t+1))
    elif func(lst) == 'o':
        print('#{} O won'.format(t+1))
    elif func(lst) == 'n':
        print('#{} Game has not completed'.format(t+1))
    elif func(lst) == 'd':
        print('#{} Draw'.format(t+1))
