X, Y = map(int, input().split())

month = (X + Y) % 12
if month == 0:
    month = 12
print(month)
