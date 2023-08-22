N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_diff = 100001
result = 0

for i in range(N):
    diff = abs(A - (T - H[i] * 0.006))
    if diff < min_diff:
        min_diff = diff
        result = i

print(result + 1)
