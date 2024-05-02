N, M = map(int, input().split())

S = [input()[-3:] for _ in range(N)]
T = [input() for _ in range(M)]

set_t = set(T)

count = 0

for s in S:
    if s in set_t:
        count += 1

print(count)