for t in range(int(input())):
    N = int(input())
    lst = list(input().split())
    result = []
    if N%2 == 0:
        for i in range(N//2):
            result.append(lst[i])
            result.append(lst[N//2+i])
    else:
        for i in range((N-1)//2):
            result.append(lst[i])
            result.append(lst[(N-1)//2+1+i])
        result.append(lst[(N-1)//2])
    print('#{} {}'.format(t+1,' '.join(result)))