N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

start = 0  # ネタの始まりのインデックスを保持する変数
ans = 0

for i in range(N):

    if B[start] <= A[i] * 2:
        ans += 1
        start += 1

    if start >= M:
        break


print(ans)
