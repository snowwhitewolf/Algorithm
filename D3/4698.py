for t in range(int(input())):
    #모든 수가 소수라고 가정하고 1이라고 주어짐
    num = [1]*(10**6+1)
    num[0] = 0
    num[1] = 0
    #모든 수에 대해서
    for i in range(2,(int((10**6+1)**0.5)+1)):
        #그 수가 소수면(아직 검증되지 않았으면)
        if num[i] == 1:
            j = 2
            #특정 숫자 i X j가 최대값보다 작으면
            while i*j <= 10**6:
                #그 수의 모든 배수는 소수가 아니므로 0
                num[i*j] = 0
                j+=1
    #처음에 2의 배수가 모두 지워지고 그다음 3의 배수 .... n의 배수를 지우면 연산 갯수가 매우 줄어든다

    
    D,A,B = map(int,(input()).split())
    result = 0
    #A~B의 숫자들중에서 소수이고 D가 포함되어있는 수의 개수를 출력
    for i in range(A,B+1):
        if num[i]:
            if str(D) in str(i):
                result += 1

    print(f'#{t+1} {result}')