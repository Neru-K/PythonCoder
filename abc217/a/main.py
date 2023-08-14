S, T = map(str, input().split())

sorted = [S, T]
sorted.sort()

if S == sorted[0]:
    print("Yes")
else:
    print("No")
