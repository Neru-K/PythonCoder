a, b, c = map(int, input().split())

w = c - (a - b)

if w < 0:
    print(0)
else:
    print(w)
