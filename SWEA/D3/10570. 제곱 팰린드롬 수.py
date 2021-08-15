lst = []

for i in range(1,32):
    a = 1
    for j in range(len(str(i))//2+1):
        if str(i)[j] != str(i)[len(str(i))-j-1]:
            a = 0
    for j in range(len(str(i*i))//2+1):
        if str(i*i)[j] != str(i*i)[len(str(i*i))-j-1]:
            a = 0
    if a == 1:
        lst.append(i*i)


for t in range(int(input())):
    cnt = 0
    A, B = map(int,input().split())
    for i in lst:
        if A <= i <= B:
            cnt += 1
    print('#{} {}'.format(t+1,cnt))