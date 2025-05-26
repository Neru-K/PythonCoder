N = int(input())
P = list(map(int, input().split()))
S = []


def rle(s):
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr


for i in range(1, N):
    if P[i - 1] < P[i]:
        S.append("<")
    else:
        S.append(">")

shortS = rle("".join(S))

count = 0

for j in range(1, len(shortS) - 1):
    if shortS[j][0] == ">" and shortS[j - 1][0] == "<" and shortS[j + 1][0] == "<":
        count += shortS[j - 1][1] * shortS[j + 1][1]

print(count)
