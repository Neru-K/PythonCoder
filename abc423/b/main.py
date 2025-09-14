N = int(input())

L = list(map(int, input().split()))

visited = [0] * (N + 1)
visited[0] = 1
visited[N] = 1

for i in range(N):
    if L[i] == 0:
        visited[i + 1] = 1
    else:
        break

for j in range(N - 1, -1, -1):
    if L[j] == 0:
        visited[j] = 1
    else:
        break

count = 0
for k in range(N + 1):
    if visited[k] == 0:
        count += 1

print(count)
