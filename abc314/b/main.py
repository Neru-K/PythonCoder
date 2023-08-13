N = int(input())

C = []

A = []

for i in range(N * 2):
    if i % 2 == 0:
        C.append(int(input()))
    else:
        A.append(list(map(int, input().split())))

X = int(input())

betNum = []
betCount = []

for j in range(N):
    if X in A[j]:
        betNum.append(j + 1)
        betCount.append(len(A[j]))

if len(betCount) == 0:
    betMin = 0
else:
    betMin = min(betCount)

result = []

for k in range(len(betCount)):
    if betCount[k] == betMin:
        result.append(str(betNum[k]))

print(len(result))
print(" ".join(result))
