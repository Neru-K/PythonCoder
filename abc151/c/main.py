N, M = map(int, input().split())

pS = [list(map(str, input().split())) for _ in range(M)]

isAccepted = set()
wacount = [0] * N
AC = 0
WA = 0

for i in range(M):
    if pS[i][0] not in isAccepted:
        if pS[i][1] == "WA":
            wacount[int(pS[i][0]) - 1] += 1
        else:
            AC += 1
            WA += wacount[int(pS[i][0]) - 1]
            isAccepted.add(pS[i][0])

print(str(AC) + " " + str(WA))
