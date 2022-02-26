for t in range(int(input())):
    a = str(input())
    result = 0
    for i in range(2, len(a)//2):
        if a[0:i] == a[i:i*2]:
            result = i
            break
    print(f'#{t+1} {result}')
