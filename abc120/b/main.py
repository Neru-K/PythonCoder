A, B, K = map(int, input().split())

array = []

for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        array.append(i)

print(array[K - 1])
