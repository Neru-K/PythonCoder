def intersect(l1, r1, l2, r2):
    return max(l1, l2) < min(r1, r2)


a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

print(
    "Yes"
    if intersect(a, d, g, j)\
    and intersect(b, e, h, k)\
    and intersect(c, f, i, l)
    else "No"
)