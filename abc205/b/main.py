N = int(input())

A = list(map(int, input().split()))

sorted = sorted(A)

array = []

for i in range(N):
    array.append(i + 1)

if array == sorted:
    print("Yes")
else:
    print("No")
