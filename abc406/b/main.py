N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1

for i in range(N):
  result *= A[i]
  if len(str(result)) > K:
    result = 1
    
print(result)