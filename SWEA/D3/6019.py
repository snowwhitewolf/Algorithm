for t in range(int(input())):
    d,a,b,f = map(int,(input()).split())
    print(f'#{t+1} {f*d/(a+b)}')