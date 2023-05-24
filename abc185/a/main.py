a = list(map(int, input().split()))

min = 101

for i in range(len(a)):
    if min > a[i]:
        min = a[i]

print(min)
