for t in range(int(input())):
    s = list(str(input().strip()))
    c = 0
    if s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        c = 1
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        c = 1
    elif s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        c = 1
    
    if c == 1:
        print('#{} Yes'.format(t+1))
    else:
        print('#{} No'.format(t+1))