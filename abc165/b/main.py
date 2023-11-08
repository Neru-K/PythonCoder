import math

X = int(input())

count = 0
price = 100

while price < X:
    price += math.floor(price * 0.01)
    count += 1

print(count)
