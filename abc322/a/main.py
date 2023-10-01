N = int(input())
S = input()

result = -1

for i in range(N - 2):
    if S[i] + S[i + 1] + S[i + 2] == "ABC":
        result = i + 1
        break

print(result)
