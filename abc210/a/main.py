n, a, x, y = map(int, input().split())
normal = 0
discounted = 0

if n < a:
    normal = n * x
else:
    normal = a * x
    discounted = (n - a) * y

print(normal + discounted)
