for _ in range(10):
    t = int(input())
    lst = []
    for _ in range(100):
        lst.append(list(map(int,input().split())))
        goal = 0
    for i in range(100):
        if lst[99][i] == 2:
            goal = i
    x = goal
    y = 99
    while y!=0:
        if x == 0:
            if lst[y][x + 1] == 0:
                y -= 1
            elif lst[y][x + 1] == 1:
                x += 1
                while lst[y - 1][x] != 1:
                    x += 1
                y -= 1
        elif x == 99:
            if lst[y][x - 1] == 0:
                y -= 1
            elif lst[y][x - 1] == 1:
                x -= 1
                while lst[y - 1][x] != 1:
                    x -= 1
                y -= 1
        else:
            if lst[y][x-1] == 0 and lst[y][x+1] == 0:
                y -= 1
            elif lst[y][x-1] == 1 and lst[y][x+1] == 0:
                x -= 1
                while lst[y-1][x] != 1:
                    x -= 1
                y -= 1
            elif lst[y][x - 1] == 0 and lst[y][x + 1] == 1:
                x += 1
                while lst[y - 1][x] != 1:
                    x += 1
                y -= 1
    print(f'#{t} {x}')