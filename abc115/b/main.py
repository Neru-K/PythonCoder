N = int(input())

p = [int(input()) for _ in range(N)]

max = max(p)
sum = sum(p)

print(int(sum - max / 2))
