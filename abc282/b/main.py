n, m = map(int, input().split())

s = []
result = 0

for _ in range(n):
    s.append(input())

for i in range(n):
    for j in range(i + 1, n):

        count = 0
        for k in range(m):
            if s[i][k] == "o" or s[j][k] == "o":
                count += 1

        if count == m:
            result += 1

print(result)
