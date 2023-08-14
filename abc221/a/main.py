A, B = map(int, input().split())

if A == B:
    print(1)
else:
    print(32 ** (A - B))
