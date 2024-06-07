N = int(input())
A = list(map(int, input().split()))
result = []

for i in range(N):
    while i + 1 != A[i]:
        element = [i+1, A[i]]
        result.append(element)
        tmp = A[A[i] - 1]
        A[A[i] - 1] = A[i]
        A[i] = tmp
        

print(len(result))

for j in range(len(result)):
    print(*result[j])