for t in range(int(input())):
    iron = list(map(str, input().strip()))
    s = 0
    result = 0
    for i in range(len(iron)-1):
        if iron[i] == '(' and iron[i+1] == ')':
            iron[i] = '1'
            iron[i+1] = '2'
    for i in iron:
        if i == '(':
            s += 1
        elif i == '1':
            result += s
        elif i == ')':
            s -= 1
            result += 1
    print(f'#{t+1} {result}')
