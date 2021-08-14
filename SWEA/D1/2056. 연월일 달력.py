for t in range(int(input())):
    date = str(input())
    s = 0
    if date[4:6] == '01':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '02':
        if int(date[6:8]) > 28:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '03':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '04':
        if int(date[6:8]) > 30:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '05':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '06':
        if int(date[6:8]) > 30:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '07':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '08':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '09':
        if int(date[6:8]) > 30:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '10':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '11':
        if int(date[6:8]) > 30:
            s =1
            print(f'#{t+1} -1')
    elif date[4:6] == '12':
        if int(date[6:8]) > 31:
            s =1
            print(f'#{t+1} -1')
    if s == 0 and 1<= int(date[4:6]) <= 12:
        print(f'#{t+1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
    elif s == 0:
        print(f'#{t+1} -1')