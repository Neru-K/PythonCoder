N = int(input())
S = input()

good = 0
bad = 0

for c in S:
    if c == "o":
        good += 1

    elif c == "x":
        bad += 1

if good > 0 and bad == 0:
    print("Yes")
else:
    print("No")
