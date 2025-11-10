N, M, K = map(int, input().split())

H = list(map(int, input().split()))
H.sort()
B = list(map(int, input().split()))
B.sort()

j = 0
max_count = 0

for i in range(N):

    while j < M and H[i] > B[j]:
        j += 1

    if j >= M:
        break

    max_count += 1
    j += 1


if max_count >= K:
    print("Yes")
else:
    print("No")
