s = input()
a, b = map(int, input().split())

chars = list(s)
chars[a - 1], chars[b - 1] = chars[b - 1], chars[a - 1]
result = "".join(chars)

print(result)
