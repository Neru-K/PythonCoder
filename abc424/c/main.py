from collections import defaultdict

N = int(input())

AB = []
having = defaultdict(set)
mastered = [0] * N

for i in range(N):

    A, B = map(int, input().split())
    AB.append((A, B))

    having[A].add(i + 1)
    having[B].add(i + 1)

for j in range(N):
    A = AB[j][0]
    B = AB[j][1]

    if mastered[j] == 1:
        continue

    if A == 0 and B == 0:
        mastered[j] = 1
    else:
        for h in having[j + 1]:
            mastered[h - 1] = 1

print(sum(mastered))
