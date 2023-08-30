alphabet = "abcdefghijklmnopqrstuvwxyz"

P = list(map(int, input().split()))

result = ""

for c in P:
    result += alphabet[c - 1]

print(result)
