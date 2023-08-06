x, a, b = map(int, input().split())

ad = abs(a-x)
bd = abs(b-x)

if ad < bd:
    print("A")
else:
    print("B")
