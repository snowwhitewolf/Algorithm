for t in range(int(input())):
    b, c = map(int, input().split())
    if b > c:
        print(f'#{t+1} >')
    elif b < c:
        print(f'#{t+1} <')
    else:
        print(f'#{t+1} =')