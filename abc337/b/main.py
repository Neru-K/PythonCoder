S = input()

isExs = "Yes"
idx = 0

for c in S:
    if c == "A":
        if idx > 0:
            isExs = "No"
            break
    elif c == "B":
        if idx > 1:
            isExs = "No"
            break
        else:
            idx = 1

    elif c == "C":
        idx = 2

print(isExs)
