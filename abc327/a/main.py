N = int(input())
S = input()

result = "No"

for i in range(N - 1):
    if S[i] + S[i + 1] == "ab" or S[i] + S[i + 1] == "ba":
        result = "Yes"
        break

print(result)
