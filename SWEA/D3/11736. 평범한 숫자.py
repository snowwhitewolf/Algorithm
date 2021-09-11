for t in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    for i in range(N-2):
        if lst[i+1] != max(lst[i],lst[i+1],lst[i+2]) and lst[i+1] != min(lst[i],lst[i+1],lst[i+2]):
            cnt += 1
    print('#{} {}'.format(t+1,cnt))