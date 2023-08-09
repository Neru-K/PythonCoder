n, k = map(int, input().split())

s = input()
result = ""

for i, c in enumerate(s):
    if i == k-1:
        result += c.lower()
    else:
        result += c

print(result)
