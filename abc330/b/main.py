N, L, R = map(int, input().split())
A = list(map(int, input().split()))

result = []

for a in A:
    if a < L:
        closest_num = L
    elif a > R:
        closest_num = R
    else:
        closest_num = a
    result.append(str(closest_num))

print(" ".join(result))
