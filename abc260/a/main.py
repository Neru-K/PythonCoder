s = input()
chars = list(s)

result = "-1"

for x in chars:
    if chars.count(x) == 1:
        result = x
        break

print(result)