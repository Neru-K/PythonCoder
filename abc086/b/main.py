import math

a, b = input().split()

str = a + b

if math.sqrt(int(str)).is_integer():
    print("Yes")
else:
    print("No")
