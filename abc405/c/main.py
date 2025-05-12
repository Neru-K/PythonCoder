N  = int(input())
A = list(map(int, input().split()))

ruisekiwa = [0] * N

result = 0

for i in range(N):
  result += ruisekiwa[i]  * A[i]
  if i < N - 1:
    ruisekiwa[i + 1] = A[i] + ruisekiwa[i]

print(result)