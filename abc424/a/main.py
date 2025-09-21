a, b, c = map(int, input().split())

lst = [int(a == b), int(b == c), int(a == c)]
if sum(lst) > 0:
    print("Yes")
else:
    print("No")
