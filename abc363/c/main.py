import itertools
import math



N, K = map(int,input().split())
S = input()

lst = list(S)

if len(set(lst)) == N:
    print(math.perm(N, K))
    exit()

unique = list(set(itertools.permutations(lst)))

count = 0

for i in range(len(unique)):
    flag = False
    serial = 0

    for j in range(N - K + 1):
        s = ''.join(unique[i])[j:K+j]
        pal = s[::-1]

        if s == pal:
            flag = True
            break

    if not flag:
        count += 1

print(count)