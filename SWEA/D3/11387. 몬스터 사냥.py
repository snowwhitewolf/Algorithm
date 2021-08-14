for t in range(int(input())):
    D,L,N = map(int,input().split())
    result = D*N
    for i in range(1,N):
        result += int(D*i*L/100)
    
    print(f'#{t+1} {result}')