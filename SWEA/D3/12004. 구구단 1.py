lst = []
for i in range(1,10):
    for j in range(1,10):
        lst.append(i*j)
for t in range(int(input())):
    a = int(input())
    if a in lst:
        print(f'#{t+1} Yes')
    else:
        print(f'#{t+1} No')