N = int(input())
A = list(map(int, input().split()))

mx = 0
sum = 0

for i in range(N):
    if A[i] > mx:
        mx = A[i]
    elif A[i] < mx:
        sum += mx - A[i]

print(sum)
