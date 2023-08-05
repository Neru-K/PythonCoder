n = int(input())
a = int(input())

if a == 0 and n % 500 == 0:
    print("Yes")
elif (n % 500) < a:
    print("Yes")
else:
    print("No")
