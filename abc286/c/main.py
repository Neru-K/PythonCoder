n, a, b = map(int, input().split())
s = input()
s += s  # シフトさせるため
ans = 1 << 60
for i in range(n):
    tmp = a * i
    for j in range(n // 2):  # n//2 除算の結果を整数に丸めた商を返す
        if s[i + j] != s[i + n - 1 - j]:
            tmp += b
    ans = min(ans, tmp)
print(ans)
