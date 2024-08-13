import itertools

S,K = map(str, input().split())

K = int(K)

arr = list(S)

perm = list(itertools.permutations(arr))

set_p = list(set(perm))
set_p.sort()

print(''.join(set_p[K-1]))