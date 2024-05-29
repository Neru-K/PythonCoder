S = input()
T = input()

lst = list('atcoder')
setc = set()
for c in lst:
    setc.add(ord(c) - 96)

arrs = [0] * 27
arrt = [0] * 27

for i in range(len(S)):
    if S[i] == '@':
        arrs[0] += 1
    else:
        arrs[ord(S[i]) - 96] += 1

    if T[i] == '@':
        arrt[0] += 1
    else:
        arrt[ord(T[i]) - 96] += 1

for i in range(1,27):
    if arrs[i] == arrt[i]:
        continue

    if i not in setc:
        print("No")
        exit()
    
    if arrs[i] > arrt[i]:
        diff = arrs[i] - arrt[i]

        if arrt[0] >= diff:
            arrt[0] -= diff
        else:
            print("No")
            exit()

    elif arrs[i] < arrt[i]:
        diff = arrt[i] - arrs[i]

        if arrs[0] >= diff:
            arrs[0] -= diff
        else:
            print("No")
            exit()

print("Yes")
