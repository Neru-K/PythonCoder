S = input()

count = 0

for i in range((len(S) + 1) // 2):
    if S[i] != S[len(S) - 1 - i]:
        count += 1

print(count)
