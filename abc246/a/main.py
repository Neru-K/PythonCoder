x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

uniquesx = set([x1, x2, x3])
resultx = sum(uniquesx) * 2 - (x1 + x2 + x3)

uniquesy = set([y1, y2, y3])
resulty = sum(uniquesy) * 2 - (y1 + y2 + y3)

print(" ".join([str(resultx), str(resulty)]))
