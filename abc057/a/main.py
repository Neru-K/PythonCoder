a, b = map(int, input().split())

time = a + b

if time >= 24:
    time = time - 24

print(time)
