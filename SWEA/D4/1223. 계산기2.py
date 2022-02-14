def cal(a):
    stack = []
    for i in a:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif i == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif i == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif i == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 // n1)
    return stack.pop()


for t in range(1, 11):
    l = int(input())
    n = input().rstrip()
    result = ''
    stack = []
    for i in n:
        if i.isdecimal():
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*' or i == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(i)
            elif i == '+' or i == '-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()
    print('#{} {}'.format(t, cal(result)))
