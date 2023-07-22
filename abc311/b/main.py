n, d = map(int, input().split())

s = []
result = [True] * d

for i in range(n):
    s.append(input())
    for idx, c in enumerate(s[i]):
        if c == "x":
            result[idx] = False

count = 0
max_count = 0
prev = False

for r in result:
    if r:
        count += 1

    else:
        count = 0

    if max_count < count:
        max_count = count

print(max_count)
