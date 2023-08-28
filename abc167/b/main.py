A, B, C, K = map(int, input().split())

sum = 0


if K <= A:
    sum = K
elif K <= A + B:
    sum = A
else:
    sum = A - (K - A - B)

print(sum)
