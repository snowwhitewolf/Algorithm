MAP = [list(input().rstrip()) for _ in range(8)]
res = 0
for y in range(8):
    for x in range(8):
        if (y+x) % 2 == 0 and MAP[y][x] == 'F':
            res += 1
print(res)