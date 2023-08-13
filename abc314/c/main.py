N, M = map(int, input().split())  # N 文字の長さ　M 色の数
S = input()
C = list(map(int, input().split()))


""" def replace_nth(s, n, replacement):
    return s[:n] + replacement + s[n + 1 :] """


for m in range(1, M + 1):
    replaceChar = "?"
    for n in range(N):
        if C[n] == m:
            next = S[n]
            S = S[:n] + replaceChar + S[n + 1 :]
            replaceChar = next

    S.replace("?", replaceChar)

print(S)
