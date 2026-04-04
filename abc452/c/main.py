from collections import defaultdict

N = int(input())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))

M = int(input())
dict = defaultdict(list)

Ss = []

for _ in range(M):
    S = input()
    Ss.append(S)

    for i in range(N):
        A, B = AB[i][0], AB[i][1]
        if len(S) == A:
            dict[(A, B)].append(S[B - 1])


def is_exists(s):
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
