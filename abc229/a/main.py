S = [input() for _ in range(2)]

result = "Yes"

for i in range(2):
    for j in range(2):
        if S[i][j] == "#":
            if S[1 - i][j] == "." and S[i][1 - j] == ".":
                result = "No"

print(result)
