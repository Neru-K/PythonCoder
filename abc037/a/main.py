a, b, c = map(int, input().split())

max = max(a, b)
min = min(a, b)

count = 0

count = c // min

if c % min >= max:
    count += max

print(count)
