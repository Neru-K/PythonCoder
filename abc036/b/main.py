n = int(input())

s = [input() for _ in range(n)]

result = [""] * n

for row in range(n):
    idx = 0
    for col in range(n):
        idx = col
        result[idx] = s[row][col] + result[idx]

for line in result:
    print(line)
