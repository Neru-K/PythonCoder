a = int(input())

max = 0
for i in range(int(a / 2 + 1)):
    if i * (a - i) > 0:
        max = i * (a - i)

print(max)
