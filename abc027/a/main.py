l1, l2, l3 = map(int, input().split())

max = max(l1, l2, l3)
min = min(l1, l2, l3)

print((max * 2 + min * 2) - l1 - l2 - l3)
