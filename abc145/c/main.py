import itertools
import math

N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

sum = 0

count = 0

for i in itertools.permutations(range(N)):
    dist = 0
    for j in range(N - 1):  # arr[(x,y),(x,y),(x,y)]
        x1, x2 = arr[i[j]][0], arr[i[j + 1]][0]
        y1, y2 = arr[i[j]][1], arr[i[j + 1]][1]
        dist += math.hypot(x2 - x1, y2 - y1)
    sum += dist
    count += 1

print(sum / count)
