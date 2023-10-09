N = int(input())
A = list(map(int, input().split()))

array = [[] for _ in range(N)]
result = []

for i in range(len(A)):
    array[A[i] - 1].append(i + 1)

for j in range(N):
    result.append((array[j][1], str(j + 1)))

result.sort(key=lambda x: x[0])

str = [tuple[1] for tuple in result]

print(" ".join(str))
