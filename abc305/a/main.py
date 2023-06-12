n = int(input())

if n % 5 == 0:
    print(str(int(n / 5 * 5)))
elif n % 5 < 3:
    print(str(5 * int(n / 5)))
else:
    print(str(5 * int(n / 5) + 5))
