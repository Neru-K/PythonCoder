N = int(input())
S = list(map(int, input().split()))

set_s = set()

for a in range(1,1000):
    for b in range(1,1000):
        s = (4 * a * b) + (3 * a) + (3 * b)
        if s > 1000:
            break

        set_s.add(s)

count = 0

for i in range(N):
    if S[i] not in set_s:
        count += 1

print(count) 