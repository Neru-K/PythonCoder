import copy

N = int(input())

S = []
T = []

for _ in range(N):
    S.append(input())

for _ in range(N):
    T.append(input())


rotated = copy.deepcopy(S)
min_count = 999999999

for c in range(4):

    count = 0

    if c > 0:
        rotated = [col[::-1] for col in zip(*rotated)]

    for i in range(N):
        row = rotated[i]
        for j in range(N):
            if T[i][j] != row[j]:
                count += 1

    count += c

    if count < min_count:
        min_count = count

print(min_count)
