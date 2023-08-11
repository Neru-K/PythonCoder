a, b = map(int,input().split())

num = a - (b * 2)

if num < 0:
    print(0)
else:
    print(num)