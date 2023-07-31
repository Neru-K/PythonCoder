a, b = map(int, input().split())

if a < 0:
    a = a + 1

if b < 0:
    b = b + 1

print(b - a)
