N = int(input())

ST = [list(map(str, input().split())) for _ in range(N)]

set = set()

max = 0

maxIndexes = 0

for i in range(N):
    if ST[i][0] not in set:
        set.add(ST[i][0])
        point = int(ST[i][1])
        if max < point:
            max = point
            maxIndexes = i

print(maxIndexes + 1)
