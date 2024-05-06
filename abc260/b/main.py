N, X, Y, Z = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
pairs = []
sorted_pairs2 = []

for i in range(N):
    pairs.append([A[i], B[i], A[i] + B[i], i + 1])


sorted_pairs = sorted(pairs, key=lambda x: (-x[0], x[3]), reverse=False,)

for i in range(X):
    result.append(sorted_pairs[i][3])

if len(pairs) > X:
    pairs2 = sorted_pairs[X:]
    sorted_pairs2 = sorted(pairs2, key=lambda x: (-x[1],x[3]), reverse=False)

    for i in range(min(Y,len(sorted_pairs2))):
        result.append(sorted_pairs2[i][3])


if len(pairs) > X + Y:
    pairs3 = sorted_pairs2[Y:]
    sorted_pairs3 = sorted(pairs3, key=lambda x:(-x[2],x[3]), reverse=False)
    for i in range(min(Z,len(sorted_pairs3))):
        result.append(sorted_pairs3[i][3])

result.sort()

print(*result, sep="\n")
