from collections import defaultdict


N, K = map(int, input().split())
S = input()

dict = defaultdict(int)

for i in range(N - K + 1):
    chars = S[i : K + i]
    dict[chars] += 1

ans = []
max = 0

for s in dict:
    if dict[s] > max:
        max = dict[s]
        ans = []

    if dict[s] < max:
        continue

    ans.append(s)


ans.sort()

print(max)
print(*ans, sep=" ")
