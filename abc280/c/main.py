S = input()
T = input()

result = len(T)

for i in range(len(S)):
    if S[i] != T[i]:
        result = i + 1
        break

print(result)
