a, b = map(int, input().split())

if b == 10:
    if a == 1 or a == 9:
        print("Yes")
    else:
        print("No")
elif b == 1:
    if a == 10 or a == 2:
        print("Yes")
    else:
        print("No")
else:
    if a == b - 1 or a == b + 1:
        print("Yes")
    else:
        print("No")
