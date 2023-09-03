A, B, C, D = map(int, input().split())

start = max(A, C)
end = min(B, D)

if end - start > 0:
    print(end - start)
else:
    print(0)
