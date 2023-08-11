S = input()
T = input()

result = "Yes"

for i in range(len(S)):
    if S[i] != T[i]:
        result = "No"
        break

print(result)
