N = int(input())
S = input()

twin = 0
awin = 0

for c in S:
    if c == "T":
        twin += 1
    else:
        awin += 1

if twin > awin:
    print("T")
elif twin < awin:
    print("A")
else:
    if S[N - 1] == "A":
        print("T")
    else:
        print("A")
