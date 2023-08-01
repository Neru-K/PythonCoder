a, b, k = map(int, input().split())

count = 0
while b > a:
    b = b / k
    count += 1

print(count)
