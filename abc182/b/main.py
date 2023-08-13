n = int(input())
a = list(map(int, input().split()))

result = [0]
max = 0
maxnum = 0

for k in range(2, 1001):
    canDivideCount = 0
    for v in a:
        if k > v:
            continue
        else:
            if v % k == 0:
                canDivideCount += 1
    if canDivideCount > max:
        max = canDivideCount
        maxnum = k

print(maxnum)
