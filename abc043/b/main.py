s = input()

result = ""

for c in s:
    if c == "0":
        result += "0"
    elif c == "1":
        result += "1"
    else:
        result = result[: len(result) - 1]

print(result)
