N = int(input())
A = list(map(int,input().split()))
A.sort()

card_count = [0] * N

for i in range(len(A)):
    card_count[A[i] - 1] += 1

idx = -1
min = 5

for i in range(N):
    if card_count[i] < min:
        min = card_count[i]
        idx = i

print(idx + 1)