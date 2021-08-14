b = []
for t in range(int(input())):
    a = int(input())
    cnt = 0
    while cnt == 0:
        for j in range(1,a+1):
            if ((a*j)**0.5)%1 == 0 and int((a*j)**0.5)**2 == a*j:
                b.append(j)
                cnt = 1
                break
for i in range(1,len(b)+1):
    print('#{} {}'.format(i,b[i-1]))