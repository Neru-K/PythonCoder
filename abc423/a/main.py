X, C = map(int, input().split())

count = 0

while X >= 1000 + C:
    X -= 1000 + C
    count += 1

print(count * 1000)
