N = int(input())
a = list(map(int, input().split()))

dict = {}

for i in range(N):
    dict[i] = a[i]

done = set()
count  = 0

for j in range(N):
    idx = a[j]
    if dict[idx] == j + 1:
        count += 1

print(count)