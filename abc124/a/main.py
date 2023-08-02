a, b = map(int, input().split())

max1 = max(a, b)
min = min(a, b)

max2 = max(max1 - 1, min)

print(max1 + max2)
