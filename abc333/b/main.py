S = input()
T = input()
d1 = abs(ord(S[0]) - ord(S[1]))
if d1 == 4:
    d1 = 1
d2 = abs(ord(T[0]) - ord(T[1]))
if d2 == 4:
    d2 = 1

if d1 == 1 and d2 == 1:
    print("Yes")
elif d1 != 1 and d2 != 1:
    print("Yes")
else:
    print("No")
