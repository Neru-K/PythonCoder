N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortedB = []

for i in range(M):
    sortedB.append((B[i], i))

sortedB.sort(reverse=True)

ans = []

idxA = 0
idxB = 0

while idxB < M:
    if idxA >= N:
        ans.append((sortedB[idxB][1], -1)) #もしAの順番がNより大きくなったら-1を返す
        idxB += 1
    elif sortedB[idxB][0] >= A[idxA]:
        ans.append((sortedB[idxB][1], idxA + 1)) #(Bの順番、Aの順番) 最後にBの順番でソートする
        idxB += 1
    else:
        idxA += 1

ans.sort()

for k in range(len(ans)):
    print(ans[k][1])