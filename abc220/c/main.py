N = int(input())
A = list(map(int, input().split()))
X = int(input())

i = 0
sum = 0
while sum <= X:
    sum += A[i % 3]
    i += 1

print(i)
