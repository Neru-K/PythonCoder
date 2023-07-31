a, b = map(int, input().split())

diff = b - a

sum = 0

for i in range(diff):
    sum += i

print(sum - a)
