from itertools import product

N, M, K = map(int, input().split()) #N本の鍵、M回のテスト、K本挿した
keys = []

allkeys = []

open = []
close = []

for i in range(M):
    row = list(map(str, input().split()))
    result = row.pop(-1)
    allkeys += row
    arr = sorted(list(set(row)))
    keys.append(arr)

unique = list(set(allkeys))


for pro in product((0, 1), repeat=N):
    # proは長さN、各要素が整数 0 か 1 のタプル
    print(pro)

