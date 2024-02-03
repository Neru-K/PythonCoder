N = int(input())
A = list(map(int, input().split()))

array = [0] * N
min = 0
result = 0

for i in range(N):
    array[i] = A[i]
    if i > 0:
        array[i] += array[i - 1]

    if array[i] < min:
        min = array[i]

result = array[len(array) - 1]
if min < 0:
    result += abs(min)
print(result)