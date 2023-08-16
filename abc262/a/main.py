Y = int(input())

y = 2 - (Y % 4)

if y < 0:
    y += 4

print(Y + y)
