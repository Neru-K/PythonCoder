a, b = map(int, input().split())

if b - a == 1:
    if (a - 1) % 3 < (b - 1) % 3:
        print("Yes")
    else:
        print("No")
else:
    print("No")
