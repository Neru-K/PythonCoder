N, R = map(int, input().split())
L = list(map(int, input().split()))

l, r = N - 1, 0

for i in range(N):
    if L[i] == 0:
        if i < l:
            l = i
        elif i > r:
            r = i

count1 = 0

for j in range(N):
    if j >= l and j <= r:
        if L[j] == 1:
            count1 += 1

if R - 1 < l:

    print(r - l + 1 + count1 + (l - (R - 1)))

elif R - 1 > r:
    print(r - l + 1 + count1 + ((R - 1) - (r + 1)))

else:
    print(r - l + 1 + count1)
