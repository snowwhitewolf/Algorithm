for tc in range(10):
    n = int(input())
    t = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        if t[i] > t[i-1] and t[i] > t[i-2] and t[i] > t[i+1] and t[i] > t[i+2]:
            if t[i-1] >= t[i-2] and t[i-1] >= t[i+1] and t[i-1] >= t[i+2]:
                result += t[i]-t[i-1]
            elif t[i-2] >= t[i-1] and t[i-2] >= t[i+1] and t[i-2] >= t[i+2]:
                result += t[i]-t[i-2]
            elif t[i+1] >= t[i-2] and t[i+1] >= t[i-1] and t[i+1] >= t[i+2]:
                result += t[i]-t[i+1]
            else:
                result += t[i]-t[i+2]

    print(f'#{tc+1} {result}')
