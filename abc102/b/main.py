N = int(input())

A = list(map(int, input().split()))

mn = min(A)
mx = max(A)

print(mx - mn)
