n = int(input())
a = list(map(int, input().split()))
p = 0

masu = [0]

for i in a:
    masu[0] = 1
    for j in range(i):
        masu.insert(0, 0)

for i in range(4, len(masu)):
    p += masu[i]

print(p)
