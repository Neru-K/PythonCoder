N = int(input())
A = list(map(int, input().split()))

K = int(input())

count = 0

for a in A:
    if K <= a:
        count += 1


print(count)
