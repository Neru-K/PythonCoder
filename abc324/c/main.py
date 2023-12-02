N, T = map(str, input().split())

count = 0
result = []

for i in range(int(N)):
    S = input()

    if S == T:
        result.append(str(i + 1))

    elif len(S) == len(T):
        diff = 0
        for j in range(len(S)):
            if S[j] != T[j]:
                diff += 1
        if diff == 1:
            result.append(str(i + 1))

    elif abs(len(S) - len(T)) == 1:
        minStr = min(S, T, key=len)
        maxStr = max(S, T, key=len)
        diff2 = 0
        l = 0

        for k in range(len(minStr)):
            while l < len(maxStr):
                if minStr[k] == maxStr[l]:
                    l += 1
                    break
                else:
                    diff2 += 1
                    l += 1

                if diff2 > 1:
                    break

        if diff2 <= 1:
            result.append(str(i + 1))

print(len(result))
print(" ".join(result))
