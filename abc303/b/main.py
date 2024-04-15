N, M = map(int, input().split())

set_a = set()

for i in range(M):
    a = list(map(int, input().split()))
    for j in range(N - 1):
        pair = [a[j], a[j + 1]]
        pair.sort()
        set_a.add((pair[0],pair[1]))

count = 0

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if not (i, j) in set_a:
            count += 1

print(count)