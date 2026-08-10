import itertools

N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

dictionary = list(itertools.permutations(P))

count = 0

for d in dictionary:
    ld = list(d)
    if ld > P and ld < Q:
        count += 1

print(count)
