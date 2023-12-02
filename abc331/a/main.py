M, D = map(int, input().split())
y, m, d = map(int, input().split())

# 日に1を加える
d += 1

# 月をまたぐ場合の処理
if d > D:
    d = 1
    m += 1

    # 年をまたぐ場合の処理
    if m > M:
        m = 1
        y += 1

print(y, m, d)
