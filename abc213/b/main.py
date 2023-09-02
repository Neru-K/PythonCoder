N = int(input())
A = list(map(int, input().split()))
min = -1
prev = min
min_num = -1
prev_num = min_num

for i in range(N):
    if prev_num > min_num:
        prev_num = min_num
        prev = min
    if A[i] > min:
        min = A[i]
        min_num = i
    elif A[i] > prev:
        prev = A[i]
        prev_num = i

print(prev_num + 1)
