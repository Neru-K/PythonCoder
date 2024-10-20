import math

N = int(input())

A = list(map(int, input().split()))

A.sort()

lst = list(set(A))

print(lst)

print(math.perm(len(lst), len(lst)))
