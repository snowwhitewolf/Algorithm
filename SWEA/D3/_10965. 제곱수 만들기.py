num = [1]*(10**7+1)
num[0] = 0
num[1] = 0
for i in range(2,(int((10**7+1)**0.5)+1)):
    if num[i] == 1:
        j = 2
        while i*j <= 10**7:
            num[i*j] = 0
            j+=1
            
result = []
for t in range(int(input())):
    a = int(input())
    i = 2
    b=1
    while a > 3164:
        cnt = 0
        if num[i]:
            while a%i == 0:
                a = a//i
                cnt += 1
            if cnt%2 == 1:
                b *= i
        i += 1
    result.append(b)
for c in range(len(result)):
    print('#{} {}'.format(c+1,result[c]))