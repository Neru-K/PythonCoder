S = input()

result = "AC"
count = 0

for i, c in enumerate(S):
    if i == 0:
        if c != "A":
            result = "WA"
            break

    elif c == "C":
        count += 1
        if i < 2 or i > len(S) - 2:
            result = "WA"
            break

        if count > 1:
            result = "WA"
            break

    elif c.isupper():
        result = "WA"
        break

if count == 0:
    result = "WA"

print(result)
