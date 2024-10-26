exit()

import math

N = int(input())

A = list(map(int, input().split()))


lst = list(set(A))
lst.sort()

print(lst)

print(math.perm(len(lst), 2))
