cnt = [0 for _ in range(int(input()))]
for i in range(1,len(cnt)+1):
    cnt[i-1] += str(i).count('3') + str(i).count('6') + str(i).count('9')
    if cnt[i-1] == 0:
        print(i, end = ' ')
    else:
        print('-'*cnt[i-1], end = ' ')