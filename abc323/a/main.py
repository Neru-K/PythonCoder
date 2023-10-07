S = input()

result = "Yes"

for i in range(1, len(S) + 1):
    if i >= 2 and i <= 16:
        if i % 2 == 0:
            if S[i - 1] == "1":
                result = "No"

print(result)
