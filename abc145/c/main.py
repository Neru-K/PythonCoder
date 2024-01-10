import itertools
import math

N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

sum = 0

# 理解に時間がかかるところ。二次元以上が絡むループ（言語化できていない）

for i in itertools.permutations(range(N)):
    dist = 0
    for j in len(i):  # arr[(x,y),(x,y),(x,y)]
        dist += math.sqrt(arr[j])
    print(i)
