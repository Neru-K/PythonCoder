import math

x, y, n = map(int, input().split())

if x * 3 < y:
    print(x * n)
else:
    print(math.floor(n / 3) * y + (n % 3) * x)
