N = int(input())
S = list(input())

pos = []

for i in range(N * 2):
    if S[i] == "A":
        pos.append(i)

diffs1 = []
diffs2 = []

for j in range(len(pos)):
    diffs1.append(abs((j * 2) - pos[j]))

for k in range(len(pos)):
    diffs2.append(abs((k * 2) + 1 - pos[k]))

print(min(sum(diffs1), sum(diffs2)))
