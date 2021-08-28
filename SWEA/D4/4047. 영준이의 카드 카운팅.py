for t in range(int(input())):
    lst = input()
    scnt = [0 for _ in range(13)]
    dcnt = [0 for _ in range(13)]
    hcnt = [0 for _ in range(13)]
    ccnt = [0 for _ in range(13)]
    error = 0
    for i in range(0,len(lst),3):
        if lst[i] == 'S':
            if scnt[int(lst[i+1:i+3])-1] == 1:
                error = 1
                break
            else:
                scnt[int(lst[i+1:i+3])-1] = 1
        elif lst[i] == 'D':
            if dcnt[int(lst[i+1:i+3])-1] == 1:
                error = 1
                break
            else:
                dcnt[int(lst[i+1:i+3])-1] = 1
        elif lst[i] == 'H':
            if hcnt[int(lst[i+1:i+3])-1] == 1:
                error = 1
                break
            else:
                hcnt[int(lst[i+1:i+3])-1] = 1
        else:
            if ccnt[int(lst[i+1:i+3])-1] == 1:
                error = 1
                break
            else:
                ccnt[int(lst[i+1:i+3])-1] = 1
    if error == 1:
        print('#{} ERROR'.format(t+1))
    else:
        print('#{} {} {} {} {}'.format(t+1,scnt.count(0),dcnt.count(0),hcnt.count(0),ccnt.count(0)))