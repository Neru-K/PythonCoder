N, X = map(int, input().split())

m = [int(input()) for _ in range(N)]

min = min(m)
sum = sum(m)
remaining = X - sum

count = N

while remaining >= min:
    remaining -= min
    count += 1

print(count)
