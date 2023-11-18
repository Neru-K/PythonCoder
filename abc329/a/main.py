S = input()
result = ""

for i, c in enumerate(S):
    if i != 0:
        result += " " + c

    else:
        result += c

print(result)
