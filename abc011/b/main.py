S = input()

result = ""

for i in range(len(S)):
    if i == 0:
        result += S[i].upper()
    else:
        result += S[i].lower()

print(result)
