S = input()

result = ""

for c in S:
    if c != "a" and c != "i" and c != "e" and c != "u" and c != "o":
        result += c

print(result)
