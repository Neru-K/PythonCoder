N = int(input())
A = list(map(int, input().split()))

u = set(A)

if len(u) == 1:
    print("Yes")
else:
    print("No")
