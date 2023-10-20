N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    won = []
    for j in range(0, len(A), 2):
        won.append(max(A[j], A[j + 1]))

print()
