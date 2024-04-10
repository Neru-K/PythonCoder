N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

setA = set(A)

result1 = 0
result2 = 0

for i in range(N):
    if A[i] == B[i]:
        result1 += 1

    elif B[i] in setA:
        result2 += 1

print(result1)
print(result2)