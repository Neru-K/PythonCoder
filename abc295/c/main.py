N = int(input())
A = list(map(int, input().split()))

pair = {}

for i in range(N):
    if A[i] not in pair:
        pair[A[i]] = 1
    else:
        pair[A[i]] += 1

count = 0

for v in pair.values():
    count += v // 2

print(count)
