a = []
for t in range(int(input())):
    A,B,C,D = map(int,input().split())

    if A/B > C/D:
        a.append('ALICE')
    elif A/B < C/D:
        a.append('BOB')
    else:
        a.append('DRAW')
for i in range(len(a)):
    print(f'#{i+1} {a[i]}')