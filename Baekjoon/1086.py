import sys
import itertools
from math import gcd

sys.stdin = open('input.txt', 'r')

N = int(input())
lst = [input() for _ in range(N)]
K = int(input())
res =0
P = list(itertools.permutations(lst, N))
total = ''
for i in range(len(P)):
    for j in range(N):
        total += P[i][j]
    if int(total) % K == 0:
        res += 1
    total = ''

if res:
    a = gcd(res,len(P))
    print("{}/{}".format(res//a,len(P)//a))
else:
    print('0/1')
