a, b = map(int, input().split())

k = (a + b) / 2

if a % 2 != b % 2:
    print("IMPOSSIBLE")
elif abs(a - k) == abs(b - k):
    print(int(k))
else:
    print("IMPOSSIBLE")
