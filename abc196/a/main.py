a, b = map(int, input().split())
c, d = map(int, input().split())

max = max(a, b)
min = min(c, d)

print(max - min)
