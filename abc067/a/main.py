a, b = map(int, input().split())

result = "Impossible"

if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
    result = "Possible"

print(result)
