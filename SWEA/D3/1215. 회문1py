for tc in range(10):
    k = int(input())
    lst = []
    cnt = 0
    for l in range(8):
        lst.append(list(map(str,input().strip())))
    
    for y in range(8):
        for x in range(9 - k):
            if lst[y][x:x+k] == lst[y][x:x+k][::-1]:
                cnt += 1

        
    for y in range(9-k):
        for x in range(8):
            A = ''
            for z in range(k):
                A += lst[y+z][x]
            if A == A[::-1]:
                cnt += 1


    print(f'#{tc+1} {cnt}')