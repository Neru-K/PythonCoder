N = int(input())
A = list(map(int, input().split()))

unique = set(A)

if len(unique) == N:
    print("YES")
else:
    print("NO")
