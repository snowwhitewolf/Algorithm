for t in range(int(input())):
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(len(lst)):
        if lst[i] < 40:
            lst[i] = 40
    total = sum(lst)//len(lst)
    print(f'#{t+1} {total}')