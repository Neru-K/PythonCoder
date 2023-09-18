N, K = map(int, input().split())
S = input()
count = 0
result = ""
for i, c in enumerate(S):
    if c == "o" and count < K:
        result += c
        count += 1
    else:
        result += "x"

print(result)
