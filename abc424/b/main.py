N, M, K = map(int, input().split())

persons = [0] * N

ans = []

for i in range(K):
    A, B = map(int, input().split())
    persons[A - 1] += 1
    if (persons[A - 1]) == M:
        ans.append(A)

if len(ans) > 0:
    print(*ans, sep=" ")
