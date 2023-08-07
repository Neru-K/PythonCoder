a, b, c, d = map(int, input().split())

count = 1

while a > 0 and c > 0:

    if count % 2 == 1:
        c -= b
    else:
        a -= d
    count += 1


if a <= 0:
    print("No")
else:
    print("Yes")
