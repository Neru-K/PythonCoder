N = int(input())
A = list(map(int, input().split()))

result = 0

for i in range(N + 1):
    count = 0
    for j in range(N):
        if A[j] >= i:
            count += 1

    if count >= i:
        result = i

print(result)
