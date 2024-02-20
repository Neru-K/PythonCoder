N = int(input())

count = 0
remainder = N

while remainder > 1:
    if remainder == 3:
        remainder - 1
    x1 = remainder // 2
    x2 = remainder - x1

    remainder = max(x1,x2)

    count += 1

print(count * N)