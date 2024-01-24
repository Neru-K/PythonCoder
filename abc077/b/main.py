import math

max = 0

N = int(input())

for i in range(1, int(math.sqrt(N)) + 1):
    sqrt = i * i
    if sqrt > max:
        max = sqrt

print(max)
