import math
for t in range(int(input())):
    N = int(input())
    result = -1
    if math.isclose(N ** (1 / 3), int(N ** (1 / 3) + 0.000000001)):
        result = int(N**(1/3)+0.000000001)
    print('#{} {}'.format(t + 1, result))