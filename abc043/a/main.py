n = int(input())

if n % 2 == 0:
    print(int((n + 1) * n / 2))
else:
    print(int((n * (n - 1) / 2) + n))
