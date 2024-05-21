import math

a, b, d = map(int, input().split())

translateX = math.sqrt(a**2 + b**2) * math.cos(math.radians(d))
translateY = math.sqrt(a**2 + b**2) * math.sin(math.radians(d))

print(*[translateX, translateY])