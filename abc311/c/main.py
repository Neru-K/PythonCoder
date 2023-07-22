n = int(input())
a = [0] + [int(x) for x in input().split()]

fl = [0] * (n+1)

s = []
v = 1
while fl[v] == 0:
    fl[v] = 1
    s.append(v)
    v = a[v]

res = []
for nx in s:
    if nx == v:
        v = -1
    if v == -1:
        res.append(nx)

print(len(res))
print(" ".join(map(str, res)))
