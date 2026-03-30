N, L, R = map(int, input().split())
S = input()

alphabets = "abcdefghijklmnopqrstuvwxyz"

ans = 0

for c in alphabets:
    ruisekiwa = [0]
    for s in S:
        if s == c:
            ruisekiwa.append(ruisekiwa[-1] + 1)
        else:
            ruisekiwa.append(ruisekiwa[-1])

    for j in range(N):
        if S[j] == c:
            l, r = max(0, j - R), j - L + 1
            if r < 0:
                continue

        ans += ruisekiwa[r] - ruisekiwa[l]
