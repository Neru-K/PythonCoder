n = int(input())

ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

distance = sum(a)
average_speed = 0

for i in range(n):
    average_speed += a[i]/b[i]

mid_speed = average_speed / 2
