N, R = map(int, input().split())
L = list(map(int, input().split()))

if not L.count(0):
    print(0)
    exit()

l, r = N - 1, 0

for i in range(N):
    if L[i] == 0:
        if i < l:
            l = i
        elif i > r:
            r = i

count1 = 0

l = min(l, R)
r = max(r + 1, R)

print(L[l:r].count(1) + (r - l))
