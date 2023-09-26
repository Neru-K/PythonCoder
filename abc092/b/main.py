N = int(input())
D, X = map(int, input().split())

count = 0

for i in range(N):
    A = int(input())
    count += ((D - 1) // A) + 1

count += X

print(count)
