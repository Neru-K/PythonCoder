import math

n = int(input())
a = list(map(int, input().split()))

sum = 0
zero_count = 0

for i in a:
    sum += i
    if i == 0:
        zero_count += 1

print(math.ceil(sum / (n - zero_count)))
