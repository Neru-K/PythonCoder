import math

# a, b = map(int, input().split())
a = 250
b = 320

print(a * 1.25)
print(b)

if math.floor(a * 1.25) == math.floor(b):
    print(int(max(a * 12.5, b * 10)))
else:
    print(-1)
