a, b, x = map(int, input().split())

if a + b == x:
    print("YES")
elif a + b > x:
    if a <= x:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
