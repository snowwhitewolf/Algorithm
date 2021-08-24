for t in range(int(input())):
    a = input()
    n = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s = ''
    for i in n:
        if a.count(i)%2 == 1:
            s += i
    if s == '':
        print('#{} Good'.format(t+1))
    else:
        print('#{} {}'.format(t+1,s))