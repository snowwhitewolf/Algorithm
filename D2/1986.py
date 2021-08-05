for t in range(int(input())):
    N=int(input())
    result = 0
    for i in range(1,N+1,2):
        result += i
        if i != N:
            result -= i+1
    print(f'#{t+1} {result}')