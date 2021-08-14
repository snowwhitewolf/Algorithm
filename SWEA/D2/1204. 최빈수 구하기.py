T = int(input())

for t in range(1,T+1):
    tt = int(input())
    student = list(map(int, input().split()))
    cnt = 0
    result = 0
    for n in range(101):
        st_cnt = student.count(n)
        if st_cnt > cnt:
            cnt = st_cnt
            result = n
        elif st_cnt == cnt:
            result = max(result, n)
        else:
            continue
    print(f'#{tt} {result}')