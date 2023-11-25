import math

D = int(input())
min_diff = D  # 最小差の初期値を D として設定

# x と y の探索範囲を設定
max_val = int(math.sqrt(D)) + 1

for x in range(max_val, -1, -1):
    if x**2 < D:
        y = int(math.sqrt(D - x**2)) + 1

        if abs((x**2 + y**2) - D) < min_diff:
            min_diff = abs((x**2 + y**2) - D)

        y = int(math.sqrt(D - x**2))

        if abs((x**2 + y**2) - D) < min_diff:
            min_diff = abs((x**2 + y**2) - D)

print(min_diff)
