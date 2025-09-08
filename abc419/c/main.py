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

max_length = max(abs(top - bottom), abs(right - left))

print(math.ceil(max_length / 2))
