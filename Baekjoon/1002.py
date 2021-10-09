for t in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**(1/2)
    if r == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == r or r1 + r2 == r:
        print(1)
    elif abs(r1 - r2) < r < (r1 + r2):
        print(2)
    else:
        print(0)