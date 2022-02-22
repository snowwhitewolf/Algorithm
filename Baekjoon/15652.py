N, M = map(int, input().split())


def f(level, s):
    if level == M:
        print(s.lstrip())
        return
    for i in range(1, N+1):
        if s and str(i) >= s[-1]:
            f(level+1, s+f' {str(i)}')
        elif level == 0:
            f(level + 1, s + f' {str(i)}')


f(0, '')
