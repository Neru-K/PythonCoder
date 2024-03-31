import math
S = input()

s = []

for i in range(len(S)):
    for j in range(i,len(S)):
        s.append(S[i:j + 1])

sets = set(s)

print(len(sets))