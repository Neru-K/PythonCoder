a1, a2, a3 = map(int, input().split())

max = max(a1, a2, a3)
min = min(a1, a2, a3)
mid = a1+a2+a3 - max - min

cost = abs(max - mid)
cost += abs(abs(mid - min))

print(cost)
