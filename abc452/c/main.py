from collections import defaultdict

N = int(input())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

M = int(input())
dict = defaultdict(set)

Ss = []

for _ in range(M):
    S = input()
    Ss.append(S)

    for i in range(N):
        A, B = AB[i][0], AB[i][1]
        if len(S) == A:
            dict[(A, B)].add(S[B - 1])


def is_exists(s):
    if len(s) != N:
        return False
    for i in range(len(s)):
        A, B = AB[i]
        if s[i] not in dict[(A, B)]:
            return False

    return True


for s in Ss:
    if is_exists(s):
        print("Yes")
    else:
        print("No")
