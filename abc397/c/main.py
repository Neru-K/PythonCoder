N = int(input())

A = list(map(int, input().split()))

remain = [0] * N
set_remain = set()
count_remain = 0

for i in range(N - 1, -1, -1):
    if A[i] not in set_remain:
        count_remain += 1

    remain[i] = count_remain
    set_remain.add(A[i])

set_a = set()
count = 0

for j in range(N):
    if A[j] not in set_a:
        count += 1

    set_a.add(A[j])

print(remain)
