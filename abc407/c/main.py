S = list(input())

diffs = []
count = len(S)

for i in range(1, len(S)):
    before = int(S[i - 1])
    after = int(S[i])
    diff = before - after

    if diff < 0:
        diff += 10

    count += diff

count += int(S[len(S) - 1])
print(count)