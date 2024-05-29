N = int(input())

A = list(map(int, input().split()))

A.sort()

evens = []
odds = []

result_even = -1
result_odd = -1

for i in range(N):
    if A[i] % 2 == 0:
        evens.append(A[i])
    else:
        odds.append(A[i])

if len(odds) > 1:
    result_odd = sum(odds[-2:])

if len(evens) > 1:
    result_even = sum(evens[-2:])

print(max(result_even, result_odd))

