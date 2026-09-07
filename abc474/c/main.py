N, Q = map(int, input().split())

P = list(map(int, input().split()))

list_a = []
is_exist = [0] * N

before = []
after = []

for _ in range(Q):
    a = int(input())
    list_a.append(a)

for i in range(Q - 1, -1, -1):
    if is_exist[list_a[i] - 1] == 0:
        after.append(list_a[i])
        is_exist[list_a[i] - 1] = 1

for p in P:
    if is_exist[p - 1] == 0:
        before.append(p)

ans = before + after[::-1]
print(*ans, sep=" ")
