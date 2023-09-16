S = input()

max = 0

for i in range(0, len(S)):
    for j in range(i + 1, len(S) + 1):
        s = S[i:j]
        if s == s[::-1] and max < len(s):
            max = len(s)

print(max)
