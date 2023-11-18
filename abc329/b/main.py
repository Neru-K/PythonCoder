N = int(input())

A = list(map(int, input().split()))

set = list(set(A))

set.sort()

print(set[len(set) - 2])
