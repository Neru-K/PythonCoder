import math

N = int(input())

INF = 1 << 60
top, right, bottom, left = INF, -1, -1, INF

array = []

for i in range(N):
    R, C = map(int, input().split())
    array.append((R, C))

    if R < top:
        top = R
    if R > bottom:
        bottom = R

    if C < left:
        left = C
    if C > right:
        right = C

midTB = top + (abs(top - bottom) // 2)  # 座標の絶対位置
midLR = left + (abs(left - right) // 2)

max_count = 0

for j in range(N):
    r_distance = abs(array[j][0] - midTB)
    c_distance = abs(array[j][1] - midLR)
    pow = r_distance**2 + c_distance**2
    dist = math.floor(pow**0.5)
    if dist > max_count:
        max_count = dist

print(max_count)
