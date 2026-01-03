from collections import defaultdict

dictn = defaultdict(int)

N = int(input())

powys = [1]

powy = 0
y = 2

while y**2 <= N:
    powy = y**2
    powys.append(powy)
    y += 1

powx = 1

for i in range(1, len(powys)):
    for j in range(i, len(powys)):
        n = i**2 + powys[j]
        if n > N:
            break
        dictn[n] += 1

ans = []

for k, v in dictn.items():
    if v == 1:
        ans.append(k)

print(len(ans))
ans.sort()
print(*ans, sep=" ")
