S = input()

double = 0
uppercount = 0
lowercount = 0

for c in S:
    if S.count(c) > 1:
        double += 1

    if c.isupper():
        uppercount += 1
    elif c.islower():
        lowercount += 1

if double == 0 and uppercount > 0 and lowercount > 0:
    print("Yes")
else:
    print("No")
