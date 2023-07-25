d, t, s = map(int, input().split())

min = d / t

if min <= s:
    print("Yes")
else:
    print("No")
