n, m = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(m)]

persons = [0] * n


for i in range(1, n + 1):
    for j in ab:
        if i == j[1]:
            persons[i - 1] += 1

count = 0
num = 0

for idx, k in enumerate(persons):
    if k == 0:
        count += 1
        num = idx + 1

if count == 0:
    print(num)
else:
    print(-1)
