'''
두 단어 사이에 단어가 없는 경우
1. Q가 P + a 인 경우
2. P의 마지막 알파벳 다음이 Q인 경우

'''
for t in range(int(input())):
    P = input().rstrip()
    Q = input().rstrip()
    result = ''
    if P + 'a' == Q:
        result = 'N'
    else:
        result = 'Y'
    print('#{} {}'.format(t+1,result))