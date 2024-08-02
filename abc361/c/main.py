N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
med = []

for i in range(N - 1):
    med.append(A[i + 1] - A[i])

med.sort()

print(med)
print(med[0:-K])

if len(med) == 0:
    print(0)
else:
    print(sum(med[0:-K]))