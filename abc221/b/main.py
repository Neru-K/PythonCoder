S = input()
T = input()
l = list(S)

if S == T:
    print("Yes")
    exit()

for i in range(len(S) - 1):
    copied = l.copy()
    c1 = copied[i]
    c2 = copied[i+1]
    copied[i] = c2
    copied[i + 1] = c1
    if ''.join(copied) == T:
        print("Yes")
        exit()

print("No")