a, b, c = map(int, input().split())

max = max(a, b, c)
min = min(a, b, c)

if b == a + b + c - max - min:
    print("Yes")
else:
    print("No")
