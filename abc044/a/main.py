n = int(input())
k = int(input())
x = int(input())
y = int(input())

normal = 0
discount = 0

if n > k:
    normal = k * x
    discount = (n - k) * y
else:
    normal = n * x

print(normal + discount)
