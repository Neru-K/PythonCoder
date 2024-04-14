S = input()
T = input()

counts = [[],[],[]]
lowerT = T.lower()

for i in range(len(S)):
    if S[i] == lowerT[0]:
        counts[0].append(i)
    if S[i] == lowerT[1]:
        counts[1].append(i)
    if S[i] == lowerT[2]:
        counts[2].append(i)

loopcount = 3

if T[-1] == "X":
    loopcount = 2


mn = -1

for i in range(loopcount):
    isLarger = False
    idxs = counts[i]

    for j in range(len(idxs)):
        if idxs[j] > mn:
            mn = idxs[j]
            isLarger = True
            break
    
    if not isLarger:
        print("No")
        exit()

print("Yes")