a, b, c = map(int, input().split())

max = max(a, b, c)
min = min(a, b, c)
mid = a + b + c - max - min

print(int(str(max) + str(mid)) + min)
