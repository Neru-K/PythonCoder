N = int(input())

S = [input() for _ in range(N)]

result = "No"

for i in range(N):
    breakFlag = False
    for j in range(i + 1, N):
        str = S[i] + S[j]
        str2 = S[j] + S[i]
        isKaibun = True
        isKaibun2 = True

        for k in range(0, len(str) // 2):
            if str[k] != str[len(str) - 1 - k]:
                isKaibun = False

        for k2 in range(0, len(str2) // 2):
            if str2[k2] != str2[len(str2) - 1 - k2]:
                isKaibun2 = False

        if isKaibun or isKaibun2:
            result = "Yes"
            breakFlag = True
            break

    if breakFlag:
        break

print(result)
