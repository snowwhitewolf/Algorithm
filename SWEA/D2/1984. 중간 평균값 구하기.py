for t in range(int(input())):
    lst = list(map(int,input().split()))
    print(f'#{t+1} {round((sum(lst)-max(lst)-min(lst))/8)}')