a, b, c = map(int, input().split())

if (a + b + c) / a == 3:
    print("No")
elif a == b or a == c or b == c:
    print("Yes")
else:
    print("No")
