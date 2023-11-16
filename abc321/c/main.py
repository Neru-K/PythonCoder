K = int(input())

ans = []
for i in range(1, 1 << 10):  # 0を含めず、1から2^10-1までの範囲でビット全探索
    s = ""
    for j in range(10):  # 各ビット位置を確認
        if (i >> j) & 1:
            s = str(j) + s  # 降順に数字を追加
    ans.append(int(s))

ans.sort()

print(ans[K])
