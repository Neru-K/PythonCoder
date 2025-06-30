T = int(input())

for i in range(T):
    N = int(input())
    S = list(map(int, input().split()))

    copied = []
    for j in range(1, N - 1):
        copied.append(S[j])

    copied.sort()

    copied = [S[0]] + copied
    copied.append(S[N - 1])

    ans = -1

    basenum = copied[0]

    for k in range(1, N):
        if copied[k] > basenum * 2:
            ans += 1
            basenum = copied[k - 1]

    if ans == -1:
        print(ans)
        exit()

print(ans + 2)


# コーナーケースがいっぱいある
# 最初にarrを作っておいて、2倍を超えたらその左を配列に追加。11 20 40 16みたいに後ろで小さい数字が出たパターンにも気をつける。
