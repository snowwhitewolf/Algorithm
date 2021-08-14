def sq(n,s):
    return n * s
for tc in range(10):
    t = int(input())
    a, b = map(int,input().split())
    aa = a
    for i in range(b-1):
        aa = sq(aa,a)
    print(f'#{t} {aa}')