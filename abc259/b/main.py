import math

a, b, d = map(int, input().split())

rad = math.radians(d)

translateX = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
translateY = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))

print(*[translateX, translateY])