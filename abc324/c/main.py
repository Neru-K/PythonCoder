N, T = map(str, input().split())

n = int(N)
count = 0
result = []

for i in range(n):
    S = input()

    if len(S) > len(T) + 1 or len(T) > len(S) + 1:
        continue

    if S == T:
        count += 1
        result.append(str(i + 1))
        continue

    elif T.startswith(S) or S.startswith(T):
        count += 1
        result.append(str(i + 1))
        continue

    elif T.endswith(S) or S.endswith(T):
        count += 1
        result.append(str(i + 1))
        continue

    mx = max(S, T)
    mn = min(S, T)
    concat = mx + mn
    cnt = 0
    idx1 = 0
    idx2 = 0

    for j in range(len(mx)):
        if mx[idx1] == mn[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            idx1 += 1
            cnt += 1
            if cnt > 1:
                break

    if cnt == 1:
        count += 1
        result.append(str(i + 1))
        continue


print(count)

print(" ".join(result))
