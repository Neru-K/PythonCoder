n, x = map(int, input().split())

if x == 1 or x == n:
    print(0)
elif x > (n / 2):
    print(n - x)
else:
    print(x - 1)
