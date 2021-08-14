for t in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    maxp = lst[-1]
    total = 0
    for i in range(N-2,-1,-1):
        if maxp > lst[i]:
            total += maxp-lst[i]
        else:
            maxp = lst[i]
    
    print(f'#{t+1} {total}')