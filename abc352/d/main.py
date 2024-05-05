N, K = map(int, input().split())
P = list(map(int,input().split()))

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

a = cmb(10, 3)

print(a)