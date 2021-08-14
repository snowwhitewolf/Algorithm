lst = []
for t in range(int(input())):
    N,Pd,Pg = map(int,input().split())
    if (Pd != 100 and Pg == 100) or (Pd != 0 and Pg == 0):
        lst.append('Broken')
    elif N >= 100:
        lst.append('Possible')
    else:
        for d in range(1,N+1):
            if (Pd*d)%100 == 0:
                lst.append('Possible')
                break
        else:
            lst.append('Broken')
for i in range(len(lst)):
    print('#{} {}'.format(i+1,lst[i]))