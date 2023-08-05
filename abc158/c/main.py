import math

# a, b = map(int, input().split())

a, b = 72, 89

y1 = a * 125
y2 = b * 100

max = max(y1, y2)
min = min(y1, y2)

if abs(math.ceil(a * 0.1) - math.ceil(b * 0.08)) == 0:
    print(math.ceil(max * 0.1))
else:
    print(-1)
