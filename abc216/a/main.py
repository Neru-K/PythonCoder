S = input()

X = S[: len(S) - 2]
Y = int(S[-1])
sign = ""

if Y <= 2:
    sign = "-"
elif Y <= 6:
    sign = ""
else:
    sign = "+"

print(X + sign)
