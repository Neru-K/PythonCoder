X, Y = map(int, input().split())

max = max(X, Y)
min = min(X, Y)

if min + 3 > max:
    print("Yes")
else:
    print("No")
