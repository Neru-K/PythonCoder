N = int(input())

A = list(map(int, input().split()))
isCalled = [False] * N


for i in range(N):
    if isCalled[i] is False:
        isCalled[A[i] - 1] = True


result = []

for j in range(len(isCalled)):
    if not isCalled[j]:
        result.append(str(j + 1))

print(len(result))
print(" ".join(result))
