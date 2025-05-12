from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
sorted_a = sorted(A)

dict = {}

sum = 0

for i in range(N):
    if sorted_a[i] not in dict:
        sum = sorted_a[i]
    else:
        sum += sorted_a[i]

    dict[sorted_a[i]] = sum

print(dict)
