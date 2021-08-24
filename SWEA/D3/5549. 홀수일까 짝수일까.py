for t in range(int(input())):
    n = input()
    if int(n[-1])%2 == 0:
        print('#{} Even'.format(t+1))
    else:
        print('#{} Odd'.format(t+1))