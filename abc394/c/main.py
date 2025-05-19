import re

S = input()
result_s = list(S)

for i in range(len(S) - 1, 0, -1):
    if "".join(result_s[i - 1 : i + 1]) == "WA":
        result_s[i - 1] = "A"
        result_s[i] = "C"

print(*result_s, sep="")
