n, s, t = map(int, input().split())
a = [int(input()) for _ in range(n)]

count = 0
weight = 0

for i in a:
    weight += i
    if weight >= s and weight <= t:
        count += 1

print(count)
