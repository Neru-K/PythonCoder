N = int(input())
a = list(map(int, input().split()))

r = N - 1
result = -1

for i in range(N - 1):
    if r - 2 < i:
        break
    diff = a[i + 1] - a[i]
    if diff > 1:
        r -= (diff - 1) * 2 % N
        result = i + diff

print(result)