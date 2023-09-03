N, X = map(int, input().split())

A = list(map(int, input().split()))

result = "Yes"
price = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        price += A[i - 1] - 1
    else:
        price += A[i - 1]

    if price > X:
        result = "No"
        break

print(result)
