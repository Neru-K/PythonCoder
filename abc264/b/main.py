R, C = map(int, input().split())

if max(abs(8 - R), abs(8 - C)) % 2 == 0:
    print("white")
else:
    print("black")